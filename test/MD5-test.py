import pytest
import os
import time
import tracemalloc
from src.MD5 import BaselineDeduplication


@pytest.mark.parametrize("name, size", [
    ("hundred", 100),
    ("threek", 300),
    ("tenk", 10000),
    ("hundredk", 100000),
])
def test_md5_baseline_with_various_sizes(name, size):
    # Set up file paths based on the dataset name and required output format
    file_path = f'../data/{name}.tsv'
    output_filename = f"../results/{size}-md5.txt"

    # Ensure results directory exists
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)

    # Start memory and runtime measurement
    tracemalloc.start()
    start_time = time.time()

    # Initialize the BaselineDeduplication with the input file
    baseline = BaselineDeduplication([file_path])

    # Run the MD5 baseline to find duplicates
    duplicates = baseline.find_duplicates()

    # Capture memory and runtime
    current, peak_memory = tracemalloc.get_traced_memory()
    runtime = time.time() - start_time
    tracemalloc.stop()

    # Prepare a set to track unique document IDs across the output
    unique_ids = set()

    # Write duplicates to the output file in the specified format
    with open(output_filename, "w") as output_file:
        for duplicate_set in duplicates:
            duplicate_set = set(duplicate_set)  # Ensure each document ID is unique within a line
            output_file.write(" ".join(map(str, duplicate_set)) + "\n")
            unique_ids.update(duplicate_set)

    # Check if the output file was created and verify the format
    with open(output_filename, "r") as f:
        lines = f.readlines()

    # Verify each line's format
    for line in lines:
        doc_ids = line.strip().split()
        assert all(
            doc_id.isdigit() for doc_id in doc_ids), "Output file format is incorrect: contains non-integer values."
        assert len(doc_ids) == len(set(doc_ids)), "Duplicate document IDs found in the same line."

    # Ensure no document ID appears more than once in the entire output file
    total_ids_in_lines = sum(len(line.strip().split()) for line in lines)
    assert len(unique_ids) == total_ids_in_lines, "Document IDs appear in multiple lines."

    # Log runtime and memory usage
    print(f"Test for `{file_path}` completed:")
    print(f"  Runtime: {runtime:.2f} seconds")
    print(f"  Peak Memory Usage: {peak_memory / (1024 ** 2):.2f} MB")

    # Print result in specified format
    print(f"Size: {size} - Time: {runtime:.2f} sec - Memory: {peak_memory / (1024 ** 2):.2f} MB\n")
