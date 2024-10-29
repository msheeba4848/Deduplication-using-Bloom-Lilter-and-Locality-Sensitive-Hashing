import argparse
import os
from LSH import lsh_nearest_neighbor, lsh_near_duplicates_from_files
from lsh_improv import lsh_improv_nearest_neighbor, lsh_improv_near_duplicates_from_files
from lsh_improv2 import lsh_optimized_nearest_neighbor, lsh_optimized_near_duplicates_from_files

def main():
    parser = argparse.ArgumentParser(
        description="Run Locality Sensitive Hashing (LSH) for duplicate detection or nearest neighbor search."
    )
    
    # Subparsers for different modes
    subparsers = parser.add_subparsers(dest="mode", required=True, help="Choose a mode: deduplication or nearest_neighbors")
    
    # Deduplication mode parser
    deduplication_parser = subparsers.add_parser("deduplication", help="Run collection deduplication")
    deduplication_parser.add_argument("--path", required=True, help="Path to the directory or file containing documents.")
    deduplication_parser.add_argument("--num_hashes", type=int, default=100, help="Number of hash functions for MinHash.")
    deduplication_parser.add_argument("--num_bands", type=int, default=20, help="Number of bands for LSH.")
    deduplication_parser.add_argument("--rows_per_band", type=int, default=5, help="Number of rows per band in LSH.")
    deduplication_parser.add_argument(
        "--algorithm", choices=["baseline", "improved", "optimized"], default="baseline",
        help="Choose the LSH algorithm version: baseline, improved, or optimized."
    )
    
    # Nearest neighbor mode parser
    nn_parser = subparsers.add_parser("nearest_neighbors", help="Run approximate nearest neighbor search")
    nn_parser.add_argument("--path", required=True, help="Path to the directory or file containing documents.")
    nn_parser.add_argument("--query_doc", required=True, help="Document content or path for nearest neighbor search.")
    nn_parser.add_argument("--num_hashes", type=int, default=100, help="Number of hash functions for MinHash.")
    nn_parser.add_argument("--num_bands", type=int, default=20, help="Number of bands for LSH.")
    nn_parser.add_argument("--rows_per_band", type=int, default=5, help="Number of rows per band in LSH.")
    nn_parser.add_argument(
        "--algorithm", choices=["baseline", "improved", "optimized"], default="baseline",
        help="Choose the LSH algorithm version: baseline, improved, or optimized."
    )

    # Parse arguments
    args = parser.parse_args()

    # Deduplication Mode
    if args.mode == "deduplication":
        if args.algorithm == "baseline":
            clusters = lsh_near_duplicates_from_files(args.path, args.num_hashes, args.num_bands, args.rows_per_band)
        elif args.algorithm == "improved":
            clusters = lsh_improv_near_duplicates_from_files(args.path, args.num_hashes, args.num_bands, args.rows_per_band)
        elif args.algorithm == "optimized":
            clusters = lsh_optimized_near_duplicates_from_files(args.path, args.num_hashes, args.num_bands, args.rows_per_band)
        
        print("Clusters (Near-Duplicates):", clusters)
    
    # Nearest Neighbor Mode
    elif args.mode == "nearest_neighbors":
        # Read query document content if it's a file path
        if os.path.isfile(args.query_doc):
            with open(args.query_doc, 'r', encoding='utf-8') as file:
                query_doc = file.read()
        else:
            query_doc = args.query_doc  # Direct content

        if args.algorithm == "baseline":
            result = lsh_nearest_neighbor(query_doc, args.path, args.num_hashes, args.num_bands, args.rows_per_band)
        elif args.algorithm == "improved":
            result = lsh_improv_nearest_neighbor(query_doc, args.path, args.num_hashes, args.num_bands, args.rows_per_band)
        elif args.algorithm == "optimized":
            result = lsh_optimized_nearest_neighbor(query_doc, args.path, args.num_hashes, args.num_bands, args.rows_per_band)
        
        print("Nearest Neighbors:", result)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
    
    
# PYTHONPATH=$(pwd) python src/lsh_cli.py deduplication --path data/hundred.tsv --algorithm improved --num_hashes 100 --num_bands 20 --rows_per_band 5
