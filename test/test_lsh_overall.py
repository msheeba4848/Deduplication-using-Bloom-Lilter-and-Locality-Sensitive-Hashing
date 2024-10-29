import os
import pytest
import time
import tracemalloc
from lsh.LSH import lsh_near_duplicates_from_files as lsh_original
from lsh.lsh_improv import lsh_near_duplicates_from_files as lsh_improv
from lsh.lsh_improv2 import lsh_near_duplicates_from_files as lsh_optimized

# Dictionary to hold the implementations
implementations = {
    "Original LSH": lsh_original,
    "Improved LSH": lsh_improv,
    "Optimized LSH": lsh_optimized
}

@pytest.mark.parametrize("path, size, num_hashes, num_bands, rows_per_band", [
    ("data/hundred.tsv", 100, 128, 32, 4),
    # Additional test cases can be added here
])
def test_lsh_near_duplicates(path, size, num_hashes, num_bands, rows_per_band):
    # Ensure the results directory exists
    os.makedirs("results/", exist_ok=True)
    print("Results directory created or already exists.")

    # Create or clear the performance.txt file
    performance_file = "results/performance.txt"
    with open(performance_file, 'w') as pf:
        pf.write("Performance Results\n")
        pf.write("=" * 20 + "\n\n")

    for name, lsh_func in implementations.items():
        print(f"Starting {name} implementation.")

        # Define the output file for the cluster results
        output_filename = os.path.join("results", f"{name.replace(' ', '_')}_{size}-lsh.txt")

        # Start tracking time and memory
        tracemalloc.start()
        start_time = time.time()

        # Run the LSH function to get clusters
        clusters = lsh_func(path, num_hashes, num_bands, rows_per_band)
        print(f"{name} generated clusters: {clusters}")

        # Stop tracking memory and time
        current, peak_memory = tracemalloc.get_traced_memory()
        runtime = time.time() - start_time
        tracemalloc.stop()

        # Write performance metrics to performance.txt
        with open(performance_file, 'a') as pf:
            pf.write(f"{name} - Size: {size}\n")
            pf.write(f"Runtime: {runtime:.2f} seconds\n")
            pf.write(f"Peak Memory Usage: {peak_memory / (1024 ** 2):.2f} MB\n\n")

        # Save clusters to the output file
        with open(output_filename, 'w') as output_file:
            for docs in clusters.values():
                output_file.write(" ".join(docs) + "\n")
                print(f"Writing {docs} to {output_filename}")

        # Console output for each implementation
        print(f"{name} - Time: {runtime:.2f} sec - Memory: {peak_memory / (1024 ** 2):.2f} MB\n")

    # Summary message for the console
    print("\nPerformance Comparison written to performance.txt")
