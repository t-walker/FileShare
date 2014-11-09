__author__ = 'Tyler'

import os
from hashing import file_2_hash, directory_2_hash


def main():
    file_1 = "test.txt"
    file_2 = "test_1.txt"
    directory_1 = os.getcwd()
    print("File 1:", file_2_hash(file_1))
    print("File 2:", file_2_hash(file_2))

    directory_hash = directory_2_hash(directory_1)

    for file in directory_hash[0]:
        print(file)

    return 0

if __name__ == "__main__":
    main()