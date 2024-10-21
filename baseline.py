import hashlib

def calculate_md5(text):
    hash_md5 = hashlib.md5()
    hash_md5.update(text.encode('utf-8'))
    return hash_md5.hexdigest()

def find_word_duplicates(file_path):
    hashes = {}
    duplicates = []

    with open(file_path, "r") as f:
        words = f.read().split()
        for word in words:
            word_hash = calculate_md5(word)

            if word_hash in hashes:
                print(f"Duplicate word found: '{word}'")
                duplicates.append(word)
            else:
                hashes[word_hash] = word

    if not duplicates:
        print("No duplicate words found.")

if __name__ == "__main__":
    file_path = input("Enter the file path to search for duplicate words: ")
    find_word_duplicates(file_path)