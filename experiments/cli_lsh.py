import argparse
import os
from LSH import lsh_near_duplicates_from_files 

def run_lsh(path, num_hashes, num_bands, rows_per_band):
    """
    Run LSH and detect duplicates.
    """
    clusters = lsh_near_duplicates_from_files(path, num_hashes, num_bands, rows_per_band)
    
    print("LSH detect duplicated documents clusters：")
    for cluster_id, docs in clusters.items():
        print(f"\nCluster {cluster_id}:")
        for doc_id in docs:
            print(f" - {doc_id}")

def main():
    parser = argparse.ArgumentParser(description="CLI for Bloom Filter and LSH duplicate detection")

    subparsers = parser.add_subparsers(dest="command")

    lsh_parser = subparsers.add_parser("lsh", help="Run LSH to detect near-duplicate documents")
    lsh_parser.add_argument("path", help="Path to the directory or file containing text documents")
    lsh_parser.add_argument("--num_hashes", type=int, default=100, help="Number of hash functions for MinHash")
    lsh_parser.add_argument("--num_bands", type=int, default=20, help="Number of bands for LSH")
    lsh_parser.add_argument("--rows_per_band", type=int, default=5, help="Rows per band for LSH")

    args = parser.parse_args()

    if args.command == "lsh":
        run_lsh(args.path, args.num_hashes, args.num_bands, args.rows_per_band)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
