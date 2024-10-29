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

The output looks like this:

```(sweetgreen) (base) isfarbaset@Isfars-MacBook-Air bloom_filter % PYTHONPATH=$(pwd) python -m bloom_filter.bin.main --size 200 --hash_count 4 --jurisdiction --file ../../data/five.tsv

Initialized Bloom Filter with size 200 and 4 hash functions.
Adding items from ../../data/five.tsv to Bloom Filter...
Adding item 'https://git-lfs.github.com/spec/v1' with hashes: [14, 76, 147, 176]
Added item: https://git-lfs.github.com/spec/v1
Adding item 'sha256:43a123206c0c1bb9e1e2b31f327536d2072a40c525b1fffbfe97d872aacdaee9' with hashes: [14, 79, 115, 150]
Added item: sha256:43a123206c0c1bb9e1e2b31f327536d2072a40c525b1fffbfe97d872aacdaee9
Adding item '134' with hashes: [33, 67, 117, 158]
Added item: 134

Finished adding items.
```
for checking membership:

```bash
PYTHONPATH=$(pwd) python -m bloom_filter.bin.main --size 200 --hash_count 4 --jurisdiction --file ../../data/five.tsv --check "item1" "item2"
```

The checking output looks like this:

```
(sweetgreen) (base) isfarbaset@Isfars-MacBook-Air bloom_filter % PYTHONPATH=$(pwd) python -m bloom_filter.bin.main --size 200 --hash_count 4 --jurisdiction --file ../../data/five.tsv --check "item1" "item2"
Initialized Bloom Filter with size 200 and 4 hash functions.
Adding items from ../../data/five.tsv to Bloom Filter...
Adding item 'https://git-lfs.github.com/spec/v1' with hashes: [14, 76, 147, 176]
Added item: https://git-lfs.github.com/spec/v1
Adding item 'sha256:43a123206c0c1bb9e1e2b31f327536d2072a40c525b1fffbfe97d872aacdaee9' with hashes: [14, 79, 115, 150]
Added item: sha256:43a123206c0c1bb9e1e2b31f327536d2072a40c525b1fffbfe97d872aacdaee9
Adding item '134' with hashes: [33, 67, 117, 158]
Added item: 134

Finished adding items.

Checking membership for specified items:
Checking item 'item1' with hashes: [41, 66, 138, 171]
Item 'item1' is in the Bloom Filter: False
Checking item 'item2' with hashes: [33, 79, 113, 185]
Item 'item2' is in the Bloom Filter: False
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

The output looks like this:

```
(sweetgreen) (base) isfarbaset@Isfars-MacBook-Air assignment-2-sweetgreen % git pull
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 3 (delta 2), reused 3 (delta 2), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 1.77 KiB | 302.00 KiB/s, done.
From https://github.com/DSAN6700-24Fall/assignment-2-sweetgreen
   75104a66..70702052  main       -> origin/main
Updating 75104a66..70702052
Fast-forward
 README.md | 395 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++------------------------------------------------------------------------------------------------
 1 file changed, 209 insertions(+), 186 deletions(-)
(sweetgreen) (base) isfarbaset@Isfars-MacBook-Air assignment-2-sweetgreen % cd src
(sweetgreen) (base) isfarbaset@Isfars-MacBook-Air src % cd bloom_filter
(sweetgreen) (base) isfarbaset@Isfars-MacBook-Air bloom_filter % PYTHONPATH=$(pwd) pytest tests/test_bloom_filter.py
==================================================================================================== test session starts =====================================================================================================
platform darwin -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/isfarbaset/Desktop/IB-DS/dsan-courses/dsan-6700/assignment-2-sweetgreen
configfile: pyproject.toml
collected 4 items                                                                                                                                                                                                            

tests/test_bloom_filter.py ....                                                                                                                                                                                        [100%]

===================================================================================================== 4 passed in 0.01s ======================================================================================================
(sweetgreen) (base) isfarbaset@Isfars-MacBook-Air bloom_filter % 

```

This runs tests on both standard and optimized Bloom Filter methods to ensure functionality across different hashing techniques.

## Lessons Learned and Challenges

Developing this Bloom Filter package brought valuable lessons in efficient data structure design and memory management. One key challenge was fine-tuning the hashing methods to balance speed and accuracy across large datasets. Experimenting with various hashing approaches highlighted the trade-offs between computational cost and collision reduction.