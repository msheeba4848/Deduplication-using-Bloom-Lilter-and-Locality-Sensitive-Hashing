import argparse
from bloom_filter import BloomFilter

def load_data(file_path):
    """Load data from a TSV file."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def main():
    parser = argparse.ArgumentParser(description="Bloom Filter testing with documents.")
    parser.add_argument("--size", type=int, required=True, help="Size of the Bloom Filter.")
    parser.add_argument("--hash_count", type=int, required=True, help="Number of hash functions.")
    parser.add_argument("--file", type=str, required=True, help="Path to the data file.")
    
    args = parser.parse_args()
    
    bloom_filter = BloomFilter(size=args.size, hash_count=args.hash_count)
    print(f"Initialized Bloom Filter with size {args.size} and {args.hash_count} hash functions.")
    
    # Load data and add to Bloom Filter
    data_items = load_data(args.file)
    print(f"Adding items from {args.file} to Bloom Filter...")
    for item in data_items:
        bloom_filter.add(item)
        print(f"Added item: {item}")
    
    print("\nFinished adding items.")

if __name__ == "__main__":
    main()