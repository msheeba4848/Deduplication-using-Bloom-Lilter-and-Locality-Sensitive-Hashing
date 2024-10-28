from .utils.hashing_methods import standard_hash, jurisdiction_hash, optimized_hash, universal_hash
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, hash_count):
        """Initialize the Bloom Filter with a given size and number of hash functions."""
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item, jurisdiction=False, optimized=False, universal=False):
        """Add an item to the Bloom Filter with a specified hashing method."""
        # Normalize item for consistent hashing
        item = item.strip().lower()
        
        if jurisdiction:
            hash_list = jurisdiction_hash(item, self.size, self.hash_count)
        elif optimized:
            hash_list = optimized_hash(item, self.size, self.hash_count)
        elif universal:
            hash_list = universal_hash(item, self.size, self.hash_count)
        else:
            hash_list = standard_hash(item, self.size, self.hash_count)

        print(f"Adding item '{item}' with hashes: {hash_list}")
        for hashed in hash_list:
            self.bit_array[hashed] = True

    def check(self, item, jurisdiction=False, optimized=False, universal=False):
        """Check if an item is in the Bloom Filter with a specified hashing method."""
        # Normalize item for consistent hashing
        item = item.strip().lower()
        
        if jurisdiction:
            hash_list = jurisdiction_hash(item, self.size, self.hash_count)
        elif optimized:
            hash_list = optimized_hash(item, self.size, self.hash_count)
        elif universal:
            hash_list = universal_hash(item, self.size, self.hash_count)
        else:
            hash_list = standard_hash(item, self.size, self.hash_count)

        print(f"Checking item '{item}' with hashes: {hash_list}")
        for hashed in hash_list:
            if not self.bit_array[hashed]:
                return False
        return True