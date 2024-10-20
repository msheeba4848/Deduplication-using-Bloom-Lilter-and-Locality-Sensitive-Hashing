[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SVDBZgP4)

# **Duplicate Detection Using Bloom Filters and Locality Sensitive Hashing (LSH)**

## **Project Overview**
This project is focused on building a solution for detecting near-duplicate documents using **Bloom filters** and **Locality Sensitive Hashing (LSH)**. The goal is to efficiently identify documents that are either identical or very similar within a large collection, while also experimenting with optimizations to improve the accuracy and speed of the solution.

## **Project Structure**
The project is organized into the following main components:

1. **Baseline Approach**:
   - A simple method for exact duplicate detection using MD5 hashes of documents.

2. **Bloom Filter Implementation**:
   - A probabilistic data structure for detecting duplicates with some false positives but no false negatives.
   - Includes optimizations and experiments to reduce false positives.

3. **Locality Sensitive Hashing (LSH)**:
   - An algorithm for near-duplicate detection, grouping similar documents into clusters.
   - Includes optimizations to speed up minhashing and improve clustering.

## **Getting Started**
### **Prerequisites**
- Python 3.x
- Poetry (for dependency management)
- Git (for version control)
  
### **Setting Up the Project**
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. **Create and activate the virtual environment** named `sweetgreen`:
   - **For macOS/Linux**:
     - Create the virtual environment:
       ```bash
       python3 -m venv sweetgreen
       ```
     - Activate the virtual environment:
       ```bash
       source sweetgreen/bin/activate
       ```
   - **For Windows**:
     - Create the virtual environment:
       ```bash
       python -m venv sweetgreen
       ```
     - Activate the virtual environment:
       ```bash
       sweetgreen\Scripts\activate
       ```

3. **Install dependencies**:
   - Install all required packages using the `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the tests**:
    ```bash
    pytest
    ```

5. **Deactivate the virtual environment when done**:
   - Deactivate the virtual environment by running:
     ```bash
     deactivate
     ```

## **Planned Features**
- **Baseline Detection**: Implement a basic MD5 hashing approach for exact duplicate detection.
- **Bloom Filter**: Implement a Bloom filter for detecting duplicates.
- **Locality Sensitive Hashing (LSH)**: Implement LSH for near-duplicate detection with document clustering.
- **Optimizations**: Explore and experiment with improvements to both the Bloom filter and LSH algorithms.

## **Project Workflow**
- We follow GitHub's best practices:
  - Use **feature branches** for development.
  - Submit changes via **pull requests**.
  - Collaborate through **issue tracking** for tasks, bugs, and improvements.
  - Automated testing and CI/CD pipelines using **GitHub Actions**.

### **GitHub Actions Setup**
1. **Create a GitHub Actions workflow**:
   - Create a file at `.github/workflows/ci.yml` with the following content:
     ```yaml
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

2. **Commit and push the workflow file**:
   - Add the workflow file to Git, commit it, and push it to the repository:
     ```bash
     git add .github/workflows/ci.yml
     git commit -m "Add GitHub Actions workflow for CI"
     git push
     ```

## **Project Structure**
The project is organized as follows:

```
dsan-6700-sweetgreen/
│
├── sweetgreen/            # Virtual environment (not tracked in Git)
├── src/                   # Source code for the project
│   ├── bloom_filter.py    # Implementation of Bloom Filter
│   ├── lsh.py             # Implementation of Locality Sensitive Hashing
│   ├── dedup.py           # Baseline deduplication methods
│   └── init.py            # Initialization file for the package
│
├── tests/                 # Test suite for the project
│   ├── test_bloom_filter.py
│   ├── test_lsh.py
│   └── test_dedup.py
│
├── requirements.txt       # Dependencies required for the project
├── README.md              # Project documentation
├── .github/               # GitHub Actions configuration
│   └── workflows/
│       └── ci.yml         # CI workflow for automated testing
└── discussion.md          # Analysis and discussion of the results
```

## **Contributing**
- Fork the repository.
- Create a new feature branch.
- Make your changes.
- Open a pull request for review.
