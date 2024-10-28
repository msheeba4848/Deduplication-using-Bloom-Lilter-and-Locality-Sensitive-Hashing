import murmurhash
import random

def standard_hash(item, size, hash_count):
    """
    Generate multiple standard MurmurHash hashes for an item.
    Args:
        item (str): The item to hash.
        size (int): Size of the bit array.
        hash_count (int): Number of hashes to generate.
    Returns:
        list: A list of hash values.
    """
    return [murmurhash.hash(item + str(i)) % size for i in range(hash_count)]

def jurisdiction_hash(item, size, hash_count):
    """
    Jurisdictional Hashing: Split the bit array into equal-sized chunks and hash items within those chunks.
    Args:
        item (str): The item to hash.
        size (int): Size of the bit array.
        hash_count (int): Number of hashes to generate.
    Returns:
        list: A list of hash values.
    """
    chunk_size = size // hash_count
    return [(i * chunk_size + murmurhash.hash(item + str(i)) % chunk_size) for i in range(hash_count)]

def optimized_hash(item, size, hash_count):
    """
    Kirsch-Mitzenmacher Optimization: Use two hashes to derive the rest.
    Args:
        item (str): The item to hash.
        size (int): Size of the bit array.
        hash_count (int): Number of hashes to generate.
    Returns:
        list: A list of hash values.
    """
    hash1 = murmurhash.hash(item)
    hash2 = murmurhash.hash(item + "salt")
    return [(hash1 + i * hash2) % size for i in range(hash_count)]

def universal_hash(item, size, hash_count):
    """
    Universal Hashing: Generate hashes using fixed primes and seeds.
    Args:
        item (str): The item to hash.
        size (int): Size of the bit array.
        hash_count (int): Number of hashes to generate.
    Returns:
        list: A list of hash values.
    """
    prime = 31
    seeds = [123, 456, 789, 101112]
    return [(murmurhash.hash(item + str(seeds[i % len(seeds)])) * prime + i) % size for i in range(hash_count)]