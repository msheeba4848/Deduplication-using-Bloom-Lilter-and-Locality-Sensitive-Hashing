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

2. **Set up a virtual environment**:
    ```bash
    poetry install
    ```

3. **Run the tests**:
    ```bash
    pytest
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

## **Contributing**
- Fork the repository.
- Create a new feature branch.
- Make your changes.
- Open a pull request for review.
