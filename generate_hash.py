import hashlib

def generate_hash(data, algorithm):
    hasher = hashlib.new(algorithm)
    data_bytes = data.encode('utf-8')
    hasher.update(data_bytes)
    return hasher.hexdigest()

def main():
    data = input("Enter data to hash: ")

    algorithm_map = {
            "1": "md5",
            "2": "sha1",
            "3": "sha224",                             "4": "sha256",
            "5": "sha384",
            "6": "sha512",
            "7": "blake2b",
            "8": "blake2s",
            "9": "sha3_224",
            "10": "sha3_256",
            "11": "sha3_384",
            "12": "sha3_512"
            }
    while True:
        print("\nChoose a hash algorithm:")
        for key, algo in algorithm_map.items():
            print(f"{key} {algo.upper()}")
        choice = input("Enter your choice (1-12): ")
        algorithm = algorithm_map.get(choice)
        if algorithm:
            hash_result = generate_hash(data, algorithm)
            print("\nHash:", hash_result)
            break;
        else:
            print("\nInvalid choice.")
            return main()

if __name__ == "__main__":
    main()
