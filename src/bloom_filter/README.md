# Bloom Filter Package

This package provides an implementation of a Bloom Filter, a probabilistic data structure useful for efficiently checking the existence of an item within a dataset. The Bloom Filter package supports multiple hashing methods and allows customization of filter size and the number of hash functions. It is structured to support testing, experimentation, and comparison between standard and improved Bloom Filters.

## Package Structure

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

## Installation

1. **Clone the repository**:  
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the package directory**
    ```
    cd bloom_filter
    ```

3. **Install dependencies:**
    ```
    pip install -r requirements.txt

    ```

## Usage

Run Bloom Filter with Command-Line Interface (CLI)

The main CLI for testing the Bloom Filter can be run as follows:

```bash
python -m bloom_filter.bin.main --size <SIZE> --hash_count <COUNT> [--jurisdiction] [--optimized] [--universal] --file <DATA_FILE>
```
	•	--size: Specify the size of the Bloom Filter.
	•	--hash_count: Set the number of hash functions.
	•	--jurisdiction, --optimized, --universal: Choose a specific hashing method.
	•	--file: Path to the data file to add and check items in the Bloom Filter.

Example:

```bash
PYTHONPATH=$(pwd) python -m bloom_filter.bin.main --size 200 --hash_count 4 --jurisdiction --file ../../data/five.tsv
```

Available Hashing Methods

	1.	Standard Hashing: Multiple hash functions using MurmurHash.
	2.	Jurisdictional Hashing: Splits the bit array into equal-sized chunks.
	3.	Kirsch-Mitzenmacher Optimization: Reduces computation by deriving hashes.
	4.	Universal Hashing: Uses random primes and seeds for hash diversity.

Testing

Run the unit tests with pytest:

```bash
PYTHONPATH=$(pwd) pytest tests/test_bloom_filter.py
```
This runs tests on both standard and optimized Bloom Filter methods to ensure functionality across different hashing techniques.

## Lessons Learned and Challenges

Developing this Bloom Filter package brought valuable lessons in efficient data structure design and memory management. One key challenge was fine-tuning the hashing methods to balance speed and accuracy across large datasets. Experimenting with various hashing approaches highlighted the trade-offs between computational cost and collision reduction.