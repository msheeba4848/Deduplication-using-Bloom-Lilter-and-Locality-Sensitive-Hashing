import murmurhash
from bitarray import bitarray
import random

class BloomFilter:
    def __init__(self, size, hash_count):
        """Initialize the Bloom Filter with a given size and number of hash functions."""
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def _hashes(self, item):
        """Standard hashing using MurmurHash: Generate multiple hashes for the given item."""
        result = []
        for i in range(self.hash_count):
            hash_result = murmurhash.hash(item + str(i)) % self.size
            result.append(hash_result)
        return result

    def _hashes_jurisdiction(self, item):
        """Jurisdictional Hashing: Split the bit array into k equal-sized chunks."""
        result = []
        chunk_size = self.size // self.hash_count
        for i in range(self.hash_count):
            hash_result = murmurhash.hash(item + str(i)) % chunk_size
            result.append(i * chunk_size + hash_result)
        return result

    def _hashes_optimized(self, item):
        """Kirsch-Mitzenmacher Optimization: Use two hash functions to generate the rest."""
        hash1 = murmurhash.hash(item)
        hash2 = murmurhash.hash(item + "salt")  # Adding salt to vary the second hash
        result = [(hash1 + i * hash2) % self.size for i in range(self.hash_count)]
        return result

    def _hashes_universal(self, item):
        """Universal Hashing: Use fixed primes and seeds to generate the hash values."""
        result = []
        prime = 31
        seeds = [123, 456, 789, 101112]  # Fixed list of seeds for consistent hashing
        for i in range(self.hash_count):
            hash_result = (murmurhash.hash(item + str(seeds[i % len(seeds)])) * prime + i) % self.size
            result.append(hash_result)
        return result

    def add(self, item, jurisdiction=False, optimized=False, universal=False):
        """Add an item to the Bloom Filter using the chosen hash method."""
        if jurisdiction:
            hash_list = self._hashes_jurisdiction(item)
        elif optimized:
            hash_list = self._hashes_optimized(item)
        elif universal:
            hash_list = self._hashes_universal(item)
        else:
            hash_list = self._hashes(item)

        for hashed in hash_list:
            self.bit_array[hashed] = True

    def check(self, item, jurisdiction=False, optimized=False, universal=False):
        """Check if an item is in the Bloom Filter."""
        if jurisdiction:
            hash_list = self._hashes_jurisdiction(item)
        elif optimized:
            hash_list = self._hashes_optimized(item)
        elif universal:
            hash_list = self._hashes_universal(item)
        else:
            hash_list = self._hashes(item)

        for hashed in hash_list:
            if not self.bit_array[hashed]:
                return False
        return True



# This file defines the BloomFilter class, but since it doesn’t contain any executable logic, you will use it by importing the class in the Jupyter notebook.

# Kirsch-Mitzenmacher Optimization:
# By computing only two hashes and deriving the others, you are reducing the computational cost and potentially improving false positive rates due to better distribution.
# Jurisdictional Hashing:
# This approach divides the bit array into chunks and reduces overlap, but it may increase complexity in managing chunked indices.
    

# Run the experiments to measure the false positive rates for the standard Bloom filter, jurisdictional hashing, and Kirsch-Mitzenmacher optimizations.
# Provide a discussion on which approaches led to significant improvements (or not).

