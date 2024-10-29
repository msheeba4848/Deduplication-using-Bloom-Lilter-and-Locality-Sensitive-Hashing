import os
import pytest
import time
import tracemalloc
from src.LSH import lsh_near_duplicates_from_files


@pytest.mark.parametrize("path, size, num_hashes, num_bands, rows_per_band", [
    ("data/hundred.tsv", 100, 128, 32, 4),
    ("data/threehundred.tsv", 300, 128, 32, 4),
 #   ("data/tenk.tsv", 10000, 128, 32, 4),
 #   ("data/hundredk.tsv", 100000, 128, 32, 4),
])
def test_lsh_near_duplicates(path, size, num_hashes, num_bands, rows_per_band):
    # Set up output filename based on parameters
    output_filename = f"results/{size}-lsh.txt"

    # Ensure results directory exists
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)

    # Start memory and runtime measurement
    tracemalloc.start()
    start_time = time.time()

    # Run LSH near-duplicate detection
    clusters = lsh_near_duplicates_from_files(path, num_hashes, num_bands, rows_per_band)

    # Capture memory and runtime
    current, peak_memory = tracemalloc.get_traced_memory()
    runtime = time.time() - start_time
    tracemalloc.stop()

    # Assertions to ensure clusters were formed
    assert len(clusters) > 0, "Expected clusters but found none."
    assert any(
        len(docs) > 1 for docs in clusters.values()), "Expected at least one cluster with more than one document."

    # Write clusters to the output file in the required format
    with open(output_filename, 'w') as output_file:
        for docs in clusters.values():
            output_file.write(" ".join(docs) + "\n")

    # Log memory and runtime results
    print(f"Test for `{path}` completed:")
    print(f"  Runtime: {runtime:.2f} seconds")
    print(f"  Peak Memory Usage: {peak_memory / (1024 ** 2):.2f} MB")

    # Print result in specified format
    print(f"Size: {size} - Time: {runtime:.2f} sec - Memory: {peak_memory / (1024 ** 2):.2f} MB\n")

    # Check output file format
    with open(output_filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            doc_ids = line.strip().split()
            assert all(doc_id.isdigit() or doc_id.startswith("doc_") for doc_id in
                       doc_ids), "Output file format is incorrect: contains non-integer values."
            assert len(doc_ids) == len(set(doc_ids)), "Duplicate document IDs found in the same line."