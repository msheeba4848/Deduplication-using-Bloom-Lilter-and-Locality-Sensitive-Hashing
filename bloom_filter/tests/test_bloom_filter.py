import pytest
from bloom_filter.bloom_filter import BloomFilter

@pytest.fixture
def bloom_filter():
    """Fixture to initialize a Bloom Filter instance with size 100 and 3 hash functions."""
    return BloomFilter(size=100, hash_count=3)

def test_add_and_check(bloom_filter):
    """Test adding items and checking their existence in the Bloom Filter."""
    # Add items to the Bloom Filter
    bloom_filter.add("apple")
    bloom_filter.add("banana")
    bloom_filter.add("cherry")

    # Check for items that should be in the filter
    assert bloom_filter.check("apple") is True
    assert bloom_filter.check("banana") is True
    assert bloom_filter.check("cherry") is True

    # Check for an item that should not be in the filter
    assert bloom_filter.check("date") is False

def test_jurisdictional_hashing(bloom_filter):
    """Test the jurisdictional hashing option."""
    bloom_filter.add("apple", jurisdiction=True)
    assert bloom_filter.check("apple", jurisdiction=True) is True
    assert bloom_filter.check("banana", jurisdiction=True) is False

def test_optimized_hashing(bloom_filter):
    """Test the Kirsch-Mitzenmacher optimized hashing option."""
    bloom_filter.add("apple", optimized=True)
    assert bloom_filter.check("apple", optimized=True) is True
    assert bloom_filter.check("banana", optimized=True) is False

def test_universal_hashing(bloom_filter):
    """Test the universal hashing option."""
    bloom_filter.add("apple", universal=True)
    assert bloom_filter.check("apple", universal=True) is True
    assert bloom_filter.check("banana", universal=True) is False