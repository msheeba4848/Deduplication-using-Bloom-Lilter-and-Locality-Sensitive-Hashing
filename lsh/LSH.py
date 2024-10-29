import os
import random
import itertools

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

    def _get_shingles(self, document, k=5):
        """Generate k-shingles (substrings of length k) for the document."""
        return set(document[i:i + k] for i in range(len(document) - k + 1))

class LSH:
    def __init__(self, num_bands, rows_per_band):
        self.num_bands = num_bands
        self.rows_per_band = rows_per_band
        self.buckets = [{} for _ in range(num_bands)]

    def hash_signature(self, doc_id, signature):
        """Hash signature into buckets using banding, adding doc_id to each bucket."""
        for i in range(self.num_bands):
            band = tuple(signature[i * self.rows_per_band:(i + 1) * self.rows_per_band])
            if band not in self.buckets[i]:
                self.buckets[i][band] = []
            self.buckets[i][band].append(doc_id)

    def find_candidates(self):
        """Return candidate pairs from buckets."""
        candidate_pairs = set()
        for band_buckets in self.buckets:
            for bucket in band_buckets.values():
                if len(bucket) > 1:
                    for pair in itertools.combinations(bucket, 2):
                        candidate_pairs.add(pair)
        return candidate_pairs

    def find_candidates_for_query(self, query_signature):
        """Find candidate pairs for a query signature."""
        candidate_pairs = set()
        for i in range(self.num_bands):
            band = tuple(query_signature[i * self.rows_per_band:(i + 1) * self.rows_per_band])
            if band in self.buckets[i]:
                for candidate in self.buckets[i][band]:
                    candidate_pairs.add(('query', candidate))
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
                    documents[filename] = file.read()

    elif os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as file:
            for idx, line in enumerate(file):
                documents[f"doc_{idx}"] = line.strip()
    else:
        raise ValueError("The provided path is neither a directory nor a file.")

    return documents

def lsh_nearest_neighbor(query_doc, path, num_hashes=100, num_bands=20, rows_per_band=5):
    # Read documents and initialize MinHash and LSH
    documents = read_documents_from_directory(path)
    minhash = MinHash(num_hashes)
    lsh = LSH(num_bands, rows_per_band)

    # Create signatures and apply LSH for all documents
    signatures = {doc_id: minhash.create_signature(doc) for doc_id, doc in documents.items()}
    for doc_id, signature in signatures.items():
        lsh.hash_signature(doc_id, signature)

    # Transform query document into a signature and find candidate pairs
    query_signature = minhash.create_signature(query_doc)
    candidate_pairs = lsh.find_candidates_for_query(query_signature)
    
    # Extract nearest neighbors from candidate pairs
    nearest_neighbors = [pair[1] for pair in candidate_pairs if pair[0] == 'query']
    return nearest_neighbors

def lsh_near_duplicates_from_files(path, num_hashes=100, num_bands=20, rows_per_band=5):
    # Read documents from the directory or file
    documents = read_documents_from_directory(path)

    # Initialize MinHash and LSH
    minhash = MinHash(num_hashes)
    lsh = LSH(num_bands, rows_per_band)

    # Create signatures and apply LSH
    signatures = {doc_id: minhash.create_signature(doc) for doc_id, doc in documents.items()}
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
