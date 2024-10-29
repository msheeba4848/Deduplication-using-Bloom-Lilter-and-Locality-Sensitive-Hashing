[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SVDBZgP4)

# **Duplicate Detection Using Bloom Filters and Locality Sensitive Hashing (LSH)**

## **Project Overview**

This project is focused on building a solution for detecting near-duplicate documents using **Bloom filters** and **Locality Sensitive Hashing (LSH)**. The goal is to efficiently identify documents that are either identical or very similar within a large collection, while also experimenting with optimizations to improve the accuracy and speed of the solution.

## **Project Structure**

The project is organized into the following main components:

1.  **Baseline Approach**:
    -   A simple method for exact duplicate detection using MD5 hashes of documents.
2.  **Bloom Filter Implementation**:
    -   A probabilistic data structure for detecting duplicates with some false positives but no false negatives.
    -   Includes optimizations and experiments to reduce false positives.
3.  **Locality Sensitive Hashing (LSH)**:
    -   An algorithm for near-duplicate detection, grouping similar documents into clusters.
    -   Includes optimizations to speed up minhashing and improve clustering.

## **Getting Started**

### **Prerequisites**

-   Python 3.x
-   Poetry (for dependency management)
-   Git (for version control)

### **Setting Up the Project**

1.  **Clone the repository**: `bash     git clone https://github.com/yourusername/yourrepository.git     cd yourrepository`

2.  **Create and activate the virtual environment** named `sweetgreen`:

    -   **For macOS/Linux**:
        -   Create the virtual environment:

            ``` bash
            python3 -m venv sweetgreen
            ```

        -   Activate the virtual environment:

            ``` bash
            source sweetgreen/bin/activate
            ```
    -   **For Windows**:
        -   Create the virtual environment:

            ``` bash
            python -m venv sweetgreen
            ```

        -   Activate the virtual environment:

            ``` bash
            sweetgreen\Scripts\activate
            ```

3.  **Install dependencies**:

    -   Install all required packages using the `requirements.txt` file:

        ``` bash
        pip install -r requirements.txt
        ```

4.  **Run the tests**: `bash     pytest`

5.  **Deactivate the virtual environment when done**:

    -   Deactivate the virtual environment by running:

        ``` bash
        deactivate
        ```

## **Planned Features**

-   **Baseline Detection**: Implement a basic MD5 hashing approach for exact duplicate detection.
-   **Bloom Filter**: Implement a Bloom filter for detecting duplicates.
-   **Locality Sensitive Hashing (LSH)**: Implement LSH for near-duplicate detection with document clustering.
-   **Optimizations**: Explore and experiment with improvements to both the Bloom filter and LSH algorithms.

## **Project Workflow**

-   We follow GitHub's best practices:
    -   Use **feature branches** for development.
    -   Submit changes via **pull requests**.
    -   Collaborate through **issue tracking** for tasks, bugs, and improvements.
    -   Automated testing and CI/CD pipelines using **GitHub Actions**.

### **GitHub Actions Setup**

1.  **Create a GitHub Actions workflow**:
    -   Create a file at `.github/workflows/ci.yml` with the following content:

        ``` yaml
        name: CI

        on:
          push:
            branches:
              - main
          pull_request:
            branches:
              - main

        jobs:
          build:
            runs-on: ubuntu-latest

            steps:
            - name: Checkout code
              uses: actions/checkout@v3

            - name: Set up Python
              uses: actions/setup-python@v4
              with:
                python-version: '3.x'

            - name: Install dependencies
              run: |
                python -m venv sweetgreen
                source sweetgreen/bin/activate
                pip install -r requirements.txt

            - name: Run tests
              run: |
                source sweetgreen/bin/activate
                pytest
        ```
2.  **Commit and push the workflow file**:
    -   Add the workflow file to Git, commit it, and push it to the repository:

        ``` bash
        git add .github/workflows/ci.yml
        git commit -m "Add GitHub Actions workflow for CI"
        git push
        ```

## **Project Structure**

The project is organized as follows:

Add structure

## **Contributing**

-   Fork the repository.
-   Create a new feature branch.
-   Make your changes.
-   Open a pull request for review.

------------------------------------------------------------------------

### 2. Algorithmic Description

## Algorithm Descriptions-Baseline MD5

### 1. Baseline: `MD5.py`

The baseline MD5 deduplication algorithm performs exact duplicate detection using MD5 hashes for each document. This approach includes:

-   **Loading TSV Files**: Documents are loaded from specified TSV files (assuming content is in the second column).

-   **MD5 Hashing**: Each document is converted into an MD5 hash.

-   **Duplicate Identification**: Documents with matching hashes are grouped as duplicates.

### 2. Improved: `md5_improv.py`

This enhanced version builds on the baseline by incorporating:

-   **Memory Efficiency**: Documents are loaded in chunks, reducing memory usage.

-   **Logging**: Informative logging has been added for tracking progress, including document loading and duplicate detection.

-   **Set-Based Hashing**: Uses a `set` to store unique hashes, further improving memory management.

## Algorithm Descriptions - Bloom Filter

### The Bloom Filter Package

This package provides an implementation of a Bloom Filter, a probabilistic data structure useful for efficiently checking the existence of an item within a dataset. The Bloom Filter package supports multiple hashing methods and allows customization of filter size and the number of hash functions. It is structured to support testing, experimentation, and comparison between standard and improved Bloom Filters.

### Package Structure

```         
.
├── README.md
├── __init__.py
├── __pycache__
│   ├── __init__.cpython-311.pyc
│   └── bloom_filter.cpython-311.pyc
├── bloom_filter
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-311.pyc
│   │   └── bloom_filter.cpython-311.pyc
│   ├── bin
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   └── main.cpython-311.pyc
│   │   └── main.py
│   ├── bloom_filter.py
│   ├── pytest.ini
│   └── utils
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-311.pyc
│       │   └── hashing_methods.cpython-311.pyc
│       └── hashing_methods.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-311.pyc
    │   └── test_bloom_filter.cpython-311-pytest-8.3.3.pyc
    └── test_bloom_filter.py

10 directories, 22 files
```

### Installation

1.  **Clone the repository**:

    ``` bash
    git clone <repository-url>
    ```

2.  **Navigate to the package directory** `cd bloom_filter`

3.  **Install dependencies:** \`\`\` pip install -r requirements.txt

    \`\`\`

### Usage

Run Bloom Filter with Command-Line Interface (CLI)

The main CLI for testing the Bloom Filter can be run as follows:

``` bash
python -m bloom_filter.bin.main --size <SIZE> --hash_count <COUNT> [--jurisdiction] [--optimized] [--universal] --file <DATA_FILE>
```

```         
•   --size: Specify the size of the Bloom Filter.
•   --hash_count: Set the number of hash functions.
•   --jurisdiction, --optimized, --universal: Choose a specific hashing method.
•   --file: Path to the data file to add and check items in the Bloom Filter.
```

Example:

``` bash
PYTHONPATH=$(pwd) python -m bloom_filter.bin.main --size 200 --hash_count 4 --jurisdiction --file ../../data/five.tsv
```

Available Hashing Methods

```         
1.  Standard Hashing: Multiple hash functions using MurmurHash.
2.  Jurisdictional Hashing: Splits the bit array into equal-sized chunks.
3.  Kirsch-Mitzenmacher Optimization: Reduces computation by deriving hashes.
4.  Universal Hashing: Uses random primes and seeds for hash diversity.
```

Testing

Run the unit tests with pytest:

``` bash
PYTHONPATH=$(pwd) pytest tests/test_bloom_filter.py
```

This runs tests on both standard and optimized Bloom Filter methods to ensure functionality across different hashing techniques.

### Lessons Learned and Challenges

Developing this Bloom Filter package brought valuable lessons in efficient data structure design and memory management. One key challenge was fine-tuning the hashing methods to balance speed and accuracy across large datasets. Experimenting with various hashing approaches highlighted the trade-offs between computational cost and collision reduction.

## Algorithm Descriptions - LSH

### 1. Baseline (LSH.py)

The baseline version of LSH includes: - **MinHashing**: Generates signatures for documents by hashing shingles. - **Banding Technique**: Divides signatures into bands and uses hashing to identify candidate pairs likely to be near-duplicates. - **Union-Find Clustering**: Groups documents into clusters based on candidate pairs.

### 2. Improved (lsh_improv.py)

The improved version builds on the baseline with: - **Multi-Probe LSH**: Adds slight variations (probes) to band hashes, increasing candidate pairs and improving recall. - **Adaptive Shingle Size**: Adjusts shingle size based on document length, helping to balance similarity detection for short and long documents.

### 3. Optimized (lsh_improv2.py)

The optimized version includes further enhancements: - **Parallelized Execution**: Utilizes `ThreadPoolExecutor` for faster MinHash and LSH computation. - **Cache Optimization**: Adds caching for frequently used hashes to reduce redundant computation. - **Fine-Tuned Parameters**: Allows for additional tuning of banding and hash function parameters.

## Testing

### MD5

```{bash}
pytest test/MD5-test.py
pytest test/md5-imp-test.py
```

### Bloom Filter

``` bash
PYTHONPATH=$(pwd) pytest tests/test_bloom_filter.py
```

### LSH

For testing, we use

```{bash}
pytest test/test_lsh_overall.py

```

------------------------------------------------------------------------

## Instructions to use CLI

This instruction contains two command-line interface (CLI) scripts for detecting duplicates using Bloom Filter and Locality-Sensitive Hashing (LSH).

### 1. Bloom Filter Usage

`cli.py` is the CLI script for Bloom Filter. Run it with the following command:

``` bash
python cli.py bloom hundred.tsv --size 100 --hash_count 3
```

#### Parameter Explanation

-   `hundred.tsv`: Input file containing text data.
-   `--size`: Size of the bit array in the Bloom Filter.
-   `--hash_count`: Number of hash functions to use.

This command uses Bloom Filter to detect duplicates in the `hundred.tsv` file.

#### Bloom Filter with Optimization Options

To use the different optimization options available in the Bloom Filter, you can add additional flags:

-   **Using Kirsch-Mitzenmacher Optimization**:

    ``` bash
    python cli.py bloom hundred.tsv --size 100 --hash_count 3 --optimized
    ```

-   **Using Jurisdictional Hashing**:

    ``` bash
    python cli.py bloom hundred.tsv --size 100 --hash_count 3 --jurisdiction
    ```

-   **Using Universal Hashing**:

    ``` bash
    python cli.py bloom hundred.tsv --size 100 --hash_count 3 --universal
    ```

These flags allow you to choose specific hash optimizations for Bloom Filter.

### 2. LSH Usage

1.  **Deduplication Mode** : Identifies clusters of near-duplicate documents within a dataset.

```{bash}
# Baseline Deduplication
PYTHONPATH=$(pwd) python src/lsh_cli.py deduplication --path data/hundred.tsv --algorithm baseline --num_hashes 100 --num_bands 20 --rows_per_band 5

# Improved Deduplication
PYTHONPATH=$(pwd) python src/lsh_cli.py deduplication --path data/hundred.tsv --algorithm improved --num_hashes 100 --num_bands 20 --rows_per_band 5

# Optimized Deduplication
PYTHONPATH=$(pwd) python src/lsh_cli.py deduplication --path data/hundred.tsv --algorithm optimized --num_hashes 100 --num_bands 20 --rows_per_band 5
```

2.  **Nearest Neighbour Mode** : Finds documents in the dataset that are most similar to a specified query document.

```{bash}
# Baseline Nearest Neighbors
PYTHONPATH=$(pwd) python src/lsh_cli.py nearest_neighbors --path data/hundred.tsv --query_doc data/query_doc.txt --algorithm baseline --num_hashes 100 --num_bands 20 --rows_per_band 5

# Improved Nearest Neighbors
PYTHONPATH=$(pwd) python src/lsh_cli.py nearest_neighbors --path data/hundred.tsv --query_doc data/query_doc.txt --algorithm improved --num_hashes 100 --num_bands 20 --rows_per_band 5

# Optimized Nearest Neighbors
PYTHONPATH=$(pwd) python src/lsh_cli.py nearest_neighbors --path data/hundred.tsv --query_doc data/query_doc.txt --algorithm optimized --num_hashes 100 --num_bands 20 --rows_per_band 5

```

## Final Outputs

### Bloom Filter

### LSH

------------------------------------------------------------------------

## Lessons Learnt

------------------------------------------------------------------------

### Notes

Make sure the `hundred.tsv` file is in the same directory as `cli.py` and `cli_lsh.py` so that the commands can correctly read the file data. The above commands assume the default directory configuration.