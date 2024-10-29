import pandas as pd
import hashlib
import logging

# Set up logging for the module
logging.basicConfig(level=logging.INFO)

class BaselineDeduplication:
    def __init__(self, file_paths):
        """Initialize with paths to .tsv files."""
        logging.info("Loading .tsv files...")
        self.documents = self.load_tsv_files(file_paths)
        logging.info(f"Loaded {len(self.documents)} documents.")

    def load_tsv_files(self, file_paths):
        """Load documents from multiple .tsv files in chunks to improve memory efficiency."""
        documents = []
        for file_path in file_paths:
            # Load the .tsv file in chunks and extract the second column (assumed to contain text content)
            for chunk in pd.read_csv(file_path, sep='\t', header=None, usecols=[1], chunksize=1000):
                documents.extend(chunk.iloc[:, 0])  # Extract the second column in each chunk

        return [str(doc) for doc in documents]  # Ensure all documents are strings

    def compute_md5(self, document):
        """Compute MD5 hash of a document."""
        return hashlib.md5(document.encode()).hexdigest()

    def find_duplicates(self):
        """Find exact duplicates using MD5 hashes."""
        hashes = set()  # Use a set to store unique hashes and save memory
        duplicates = []

        for doc in self.documents:
            doc_hash = self.compute_md5(doc)
            if doc_hash in hashes:
                duplicates.append(doc)  # Append duplicate document
                logging.debug(f"Duplicate found: {doc[:100]}...")  # Log first 100 chars for readability
            else:
                hashes.add(doc_hash)

        logging.info(f"Total duplicates found: {len(duplicat es)}")
        return duplicates
