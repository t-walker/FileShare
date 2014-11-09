__author__ = 'Tyler'

import os
from hashing import file_2_hash, directory_2_hash


def main():
    file_1 = "test.txt"
    file_2 = "test_1.txt"
    directory_1 = os.getcwd()
    print("File 1:", file_1, "Hash: ", file_2_hash(file_1))
    print("File 2:", file_2, "Hash: ", file_2_hash(file_2))
    print()

    directory_hash = directory_2_hash(directory_1)

    for i in range(len(directory_hash[0])):
        print("File:", directory_hash[0][i], "Hash:", directory_hash[1][i])

    return 0

if __name__ == "__main__":
    main()