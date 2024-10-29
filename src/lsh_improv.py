import os
import re
import random
import itertools
from concurrent.futures import ThreadPoolExecutor

# Text Preprocessing function
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Strip leading and trailing whitespace
    text = text.strip()
    return text

class MinHash:
    def __init__(self, num_hashes):
        self.num_hashes = num_hashes
        self.hash_funcs = self._generate_hash_funcs(num_hashes)

    def _generate_hash_funcs(self, num_hashes):
        hash_funcs = []
        for i in range(num_hashes):
            a, b = random.randint(1, 100), random.randint(1, 100)
            hash_funcs.append(lambda x, a=a, b=b: (a * hash(x) + b) % 2**32)
        return hash_funcs

    def create_signature(self, document):
        signature = []
        shingles = self._get_shingles(document)
        for hash_func in self.hash_funcs:
            min_hash = min(hash_func(shingle) for shingle in shingles)
            signature.append(min_hash)
        return signature

    def _get_shingles(self, document):
        """Generate k-shingles (substrings) for the document with adaptive shingle size based on length."""
        length = len(document)
        k = 3 if length < 100 else 5 if length < 500 else 7
        return set(document[i:i + k] for i in range(len(document) - k + 1))

class LSH:
    def __init__(self, num_bands, rows_per_band, probes=3):
        self.num_bands = num_bands
        self.rows_per_band = rows_per_band
        self.probes = probes  # Number of additional probes for multi-probe LSH
        self.buckets = [{} for _ in range(num_bands)]

    def _generate_probes(self, band_hash):
        """Generate variations of the band hash for multi-probe LSH."""
        return [tuple((val + offset) % 100 for val in band_hash) for offset in range(self.probes)]

    def hash_signature(self, doc_id, signature):
        """Hash signature into buckets using multi-probe banding."""
        for i in range(self.num_bands):
            band = tuple(signature[i * self.rows_per_band:(i + 1) * self.rows_per_band])
            probe_bands = self._generate_probes(band)  # Generate probe variants

            # Insert doc_id into each probe bucket
            for probe in probe_bands:
                if probe not in self.buckets[i]:
                    self.buckets[i][probe] = []
                self.buckets[i][probe].append(doc_id)

    def find_candidates(self):
        """Return candidate pairs from buckets."""
        candidate_pairs = set()
        for band_buckets in self.buckets:
            for bucket in band_buckets.values():
                if len(bucket) > 1:
                    for pair in itertools.combinations(bucket, 2):
                        candidate_pairs.add(pair)
        return candidate_pairs

class UnionFind:
    def __init__(self, elements):
        self.parent = {x: x for x in elements}
        self.rank = {x: 0 for x in elements}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def read_documents_from_directory(path):
    """Reads all text files in a directory or a single file and returns their content."""
    documents = {}

    if os.path.isdir(path):
        for filename in os.listdir(path):
            if filename.endswith(".txt"):
                with open(os.path.join(path, filename), 'r', encoding='utf-8') as file:
                    documents[filename] = preprocess_text(file.read())

    elif os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as file:
            for idx, line in enumerate(file):
                documents[f"doc_{idx}"] = preprocess_text(line.strip())
    else:
        raise ValueError("The provided path is neither a directory nor a file.")

    return documents

def lsh_near_duplicates_from_files(path, num_hashes=100, num_bands=20, rows_per_band=5):
    documents = read_documents_from_directory(path)
    minhash = MinHash(num_hashes)
    lsh = LSH(num_bands, rows_per_band)

    # Parallelize signature creation
    with ThreadPoolExecutor() as executor:
        signatures = {doc_id: sig for doc_id, sig in zip(documents.keys(), executor.map(minhash.create_signature, documents.values()))}

    # Insert signatures into LSH buckets
    for doc_id, signature in signatures.items():
        lsh.hash_signature(doc_id, signature)

    # Get candidate pairs and perform Union-Find
    candidate_pairs = lsh.find_candidates()
    uf = UnionFind(signatures.keys())
    for doc_id1, doc_id2 in candidate_pairs:
        uf.union(doc_id1, doc_id2)

    # Return clusters (groups of near-duplicate documents)
    clusters = {}
    for doc_id in signatures:
        root = uf.find(doc_id)
        if root not in clusters:
            clusters[root] = []
        clusters[root].append(doc_id)

    return clusters
