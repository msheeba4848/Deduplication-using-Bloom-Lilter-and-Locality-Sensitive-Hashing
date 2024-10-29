import sys
import os
import glob
import pytest
import logging
logging.basicConfig(level=logging.INFO)


# Add the project root directory to sys.path to locate 'src'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the BaselineDeduplication class from md5_improv.py
from src.md5_improv import BaselineDeduplication


def test_md5_baseline_with_duplicates():
    # List all .tsv files in the 'data' directory
    file_paths = glob.glob('data/*.tsv')  # Adjust path if necessary

    # Initialize the BaselineDeduplication class with all file paths
    baseline = BaselineDeduplication(file_paths)

    # Find duplicates
    duplicates = baseline.find_duplicates()

    # Assertion for pytest
    # Assertion to ensure duplicates are found
    assert len(duplicates) > 0, "Expected duplicates but found none."

# Log the number of duplicates
    print(f"Number of duplicates found: {len(duplicates)}")
    
# Inside test function
    logging.info(f"Number of duplicates found: {len(duplicates)}")


    # Print duplicates for debugging
    print("Duplicates found:" if duplicates else "No duplicates found.")
    for i, duplicate in enumerate(duplicates, 1):
        print(f"Duplicate {i}:")
        print(f"Document: {duplicate[:100]}...")  # Truncate long documents for cleaner display
        print("-" * 80)


#if __name__ == "__main__":
    # Run pytest if this script is executed directly
    
#    pytest.main([__file__])

# pytest -s test/md5-imp-test.py
