import hashlib
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, hash_count):
        """Initialize the Bloom Filter with a given size and number of hash functions."""
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def _hashes(self, item):
        """Generate multiple hashes for the given item."""
        result = []
        for i in range(self.hash_count):
            hash_result = int(hashlib.md5((item + str(i)).encode()).hexdigest(), 16) % self.size
            result.append(hash_result)
        return result

    def add(self, item):
        """Add an item to the Bloom Filter."""
        for hashed in self._hashes(item):
            self.bit_array[hashed] = True

    def check(self, item):
        """Check if an item is in the Bloom Filter."""
        for hashed in self._hashes(item):
            if not self.bit_array[hashed]:
                return False
        return True

# Example usage:
bf = BloomFilter(size=1000, hash_count=5)
bf.add("example")
print(bf.check("example"))  # Should return True
print(bf.check("other"))    # Might return False or True (false positive possible)


