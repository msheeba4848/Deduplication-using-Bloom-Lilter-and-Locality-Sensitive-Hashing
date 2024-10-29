import os
import pytest
import time
import tracemalloc
import matplotlib.pyplot as plt
from src.LSH import lsh_near_duplicates_from_files as lsh_original
from src.lsh_improv import lsh_improv_near_duplicates_from_files as lsh_improv
from src.lsh_improv2 import lsh_optimized_near_duplicates_from_files as lsh_optimized

# Dictionary to hold the implementations
implementations = {
    "Original LSH": lsh_original,
    "Improved LSH": lsh_improv,
    "Optimized LSH": lsh_optimized
}

# Data structure to store performance metrics for visualization
performance_data = {
    "Implementation": [],
    "Runtime (seconds)": [],
    "Peak Memory Usage (MB)": [],
    "Average Jaccard Similarity": []
}

def calculate_jaccard_similarity(doc1, doc2):
    """Calculate Jaccard similarity between two documents."""
    set1 = set(doc1.split())
    set2 = set(doc2.split())
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

def average_jaccard_similarity(clusters, documents):
    """Calculate the average Jaccard similarity for all pairs within each cluster."""
    jaccard_similarities = []
    for cluster_docs in clusters.values():
        if len(cluster_docs) > 1:
            for i in range(len(cluster_docs)):
                for j in range(i + 1, len(cluster_docs)):
                    doc1 = documents[cluster_docs[i]]
                    doc2 = documents[cluster_docs[j]]
                    jaccard_sim = calculate_jaccard_similarity(doc1, doc2)
                    jaccard_similarities.append(jaccard_sim)
    return sum(jaccard_similarities) / len(jaccard_similarities) if jaccard_similarities else 0

@pytest.mark.parametrize("path, size, num_hashes, num_bands, rows_per_band", [
    ("data/hundred.tsv", 100, 128, 32, 4),
])
def test_lsh_near_duplicates(path, size, num_hashes, num_bands, rows_per_band):
    os.makedirs("results/", exist_ok=True)

    # Create or clear the performance.txt file
    performance_file = "results/performance.txt"
    with open(performance_file, 'w') as pf:
        pf.write("Performance Results\n")
        pf.write("=" * 20 + "\n\n")

    # Read documents from file
    with open(path, 'r', encoding='utf-8') as f:
        documents = {f"doc_{i}": line.strip() for i, line in enumerate(f)}

    for name, lsh_func in implementations.items():
        print(f"Starting {name} implementation.")
        output_filename = os.path.join("results", f"{name.replace(' ', '_')}_{size}-lsh.txt")

        # Start tracking time and memory
        tracemalloc.start()
        start_time = time.time()

        # Run the LSH function
        clusters = lsh_func(path, num_hashes, num_bands, rows_per_band)
        print(f"{name} generated clusters: {clusters}")

        # Stop tracking memory and time
        current, peak_memory = tracemalloc.get_traced_memory()
        runtime = time.time() - start_time
        tracemalloc.stop()

        # Calculate average Jaccard similarity for clusters
        avg_jaccard_similarity = average_jaccard_similarity(clusters, documents)

        # Record metrics for visualization
        performance_data["Implementation"].append(name)
        performance_data["Runtime (seconds)"].append(runtime)
        performance_data["Peak Memory Usage (MB)"].append(peak_memory / (1024 ** 2))
        performance_data["Average Jaccard Similarity"].append(avg_jaccard_similarity)

        # Write performance metrics to performance.txt
        with open(performance_file, 'a') as pf:
            pf.write(f"{name} - Size: {size}\n")
            pf.write(f"Runtime: {runtime:.2f} seconds\n")
            pf.write(f"Peak Memory Usage: {peak_memory / (1024 ** 2):.2f} MB\n")
            pf.write(f"Average Jaccard Similarity: {avg_jaccard_similarity:.2f}\n\n")

        # Save clusters to the cluster output file
        with open(output_filename, 'w') as output_file:
            for docs in clusters.values():
                output_file.write(" ".join(docs) + "\n")
                print(f"Writing {docs} to {output_filename}")

        # Print per-implementation results in console for quick reference
        print(f"{name} - Time: {runtime:.2f} sec - Memory: {peak_memory / (1024 ** 2):.2f} MB - Avg. Jaccard Similarity: {avg_jaccard_similarity:.2f}")

    # Generate and save visualizations
    visualize_performance(performance_data)

def visualize_performance(data):
    """Generate bar charts for runtime, memory usage, and Jaccard similarity, saving them as PNG files."""
    plt.figure(figsize=(8, 5))
    plt.bar(data["Implementation"], data["Runtime (seconds)"], color=['blue', 'green', 'red'])
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime Comparison Across LSH Implementations")
    plt.savefig("results/runtime_comparison.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.bar(data["Implementation"], data["Peak Memory Usage (MB)"], color=['blue', 'green', 'red'])
    plt.ylabel("Peak Memory Usage (MB)")
    plt.title("Memory Usage Comparison Across LSH Implementations")
    plt.savefig("results/memory_usage_comparison.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.bar(data["Implementation"], data["Average Jaccard Similarity"], color=['blue', 'green', 'red'])
    plt.ylim(0, 1)
    plt.ylabel("Average Jaccard Similarity")
    plt.title("Average Jaccard Similarity Comparison Across LSH Implementations")
    plt.savefig("results/jaccard_similarity_comparison.png")
    plt.close()
