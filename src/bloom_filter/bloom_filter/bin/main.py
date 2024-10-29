import argparse
from bloom_filter import BloomFilter

def load_data(file_path):
    """Load data from a TSV file, ignoring any line number prefixes."""
    with open(file_path, 'r') as file:
        return [line.strip().split(maxsplit=1)[1].lower() for line in file if line.strip()]

def main():
    parser = argparse.ArgumentParser(description="Bloom Filter testing with documents.")
    parser.add_argument("--size", type=int, required=True, help="Size of the Bloom Filter.")
    parser.add_argument("--hash_count", type=int, required=True, help="Number of hash functions.")
    parser.add_argument("--file", type=str, required=True, help="Path to the data file.")
    parser.add_argument("--check", type=str, nargs="*", help="Items to check for membership in the Bloom Filter.")
    parser.add_argument("--jurisdiction", action="store_true", help="Use jurisdictional hashing.")
    parser.add_argument("--optimized", action="store_true", help="Use Kirsch-Mitzenmacher optimized hashing.")
    parser.add_argument("--universal", action="store_true", help="Use universal hashing.")
    
    args = parser.parse_args()
    
    # Initialize Bloom Filter
    bloom_filter = BloomFilter(size=args.size, hash_count=args.hash_count)
    print(f"Initialized Bloom Filter with size {args.size} and {args.hash_count} hash functions.")
    
    # Load data and add to Bloom Filter
    data_items = load_data(args.file)
    print(f"Adding items from {args.file} to Bloom Filter...")
    for item in data_items:
        bloom_filter.add(item, jurisdiction=args.jurisdiction, optimized=args.optimized, universal=args.universal)
        print(f"Added item: {item}")
    
    print("\nFinished adding items.")
    
    # Check membership for specified items
    if args.check:
        print("\nChecking membership for specified items:")
        for item in args.check:
            result = bloom_filter.check(item, jurisdiction=args.jurisdiction, optimized=args.optimized, universal=args.universal)
            print(f"Item '{item}' is in the Bloom Filter: {result}")

if __name__ == "__main__":
    main()