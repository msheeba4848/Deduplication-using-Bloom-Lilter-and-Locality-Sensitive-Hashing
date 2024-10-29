import pandas as pd
import hashlib


class BaselineDeduplication:
    def __init__(self, file_paths):
        """Initialize with paths to .tsv files."""
        self.documents = self.load_tsv_files(file_paths)

    def load_tsv_files(self, file_paths):
        """Load documents from multiple .tsv files with no headers."""
        documents = []
        for file_path in file_paths:
            # Load .tsv without headers (header=None), assuming text is in the second column (index 1)
            df = pd.read_csv(file_path, sep='\t', header=None)

            # Assuming the text content is in the second column (index 1)
            documents.extend(df.iloc[:, 1])  # Extract the second column for document text

        return [str(doc) for doc in documents]  # Ensure all documents are strings

    def compute_md5(self, document):
        """Compute MD5 hash of a document."""
        return hashlib.md5(document.encode()).hexdigest()

    def find_duplicates(self):
        """Find exact duplicates using MD5 hashes and return indices of duplicates."""
        hashes = {}  # Dictionary to store hash and list of document indices
        duplicates = []  # List to store sets of duplicate indices

        for index, doc in enumerate(self.documents):
            doc_hash = self.compute_md5(doc)
            if doc_hash in hashes:
                hashes[doc_hash].append(index)  # Append index to existing hash entry
            else:
                hashes[doc_hash] = [index]  # Create new entry for this hash

        # Collect only groups that have more than one entry (i.e., duplicates)
        for indices in hashes.values():
            if len(indices) > 1:
                duplicates.append(indices)

        return duplicates