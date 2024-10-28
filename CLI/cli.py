import argparse
import pandas as pd
from bloom_filter import BloomFilter 
import time

def run_bloom_filter(data_file, size, hash_count, jurisdiction, optimized, universal):
    with open(data_file, 'r') as f:
        data_lines = [line.strip() for line in f.readlines()]
    
    bloom_filter = BloomFilter(size, hash_count)  # initialize BloomFilter

    duplicates = []
    start_time = time.time()
    
    for item in data_lines:  # go through all
        if bloom_filter.check(item, jurisdiction=jurisdiction, optimized=optimized, universal=universal):
            duplicates.append(item)
        else:
            bloom_filter.add(item, jurisdiction=jurisdiction, optimized=optimized, universal=universal)
    
    end_time = time.time()
    
    # output
    print("Bloom Filter detect duplicate items：")
    for dup in duplicates:
        print(dup)
    print(f"\nprocessing time: {end_time - start_time:.2f} seconds")
    print(f"total {len(data_lines)} items， {len(duplicates)} repeated")

# main CLI 
def main():
    parser = argparse.ArgumentParser(description="CLI for Bloom Filter and LSH duplicate detection")
    
    subparsers = parser.add_subparsers(dest="command")
    
    bloom_parser = subparsers.add_parser("bloom", help="Run Bloom Filter to check duplicates")
    bloom_parser.add_argument("data_file", help="Path to the TSV data file")
    bloom_parser.add_argument("--size", type=int, default=1000, help="Size of the Bloom Filter bit array")
    bloom_parser.add_argument("--hash_count", type=int, default=3, help="Number of hash functions to use")
    bloom_parser.add_argument("--jurisdiction", action="store_true", help="Use jurisdictional hashing")
    bloom_parser.add_argument("--optimized", action="store_true", help="Use Kirsch-Mitzenmacher optimized hashing")
    bloom_parser.add_argument("--universal", action="store_true", help="Use universal hashing")
    
    args = parser.parse_args()
    
    if args.command == "bloom":
        run_bloom_filter(args.data_file, args.size, args.hash_count, args.jurisdiction, args.optimized, args.universal)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
