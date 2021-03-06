__author__ = 'Tyler'

import os
from hashing import file_2_hash, directory_2_hash
from filechange import file_hash_DICT

def main():
    file_1 = "test.txt"
    file_2 = "test_1.txt"
    directory_1 = os.getcwd()
    print("File 1:", file_1, "Hash: ", file_2_hash(file_1))
    print("File 2:", file_2, "Hash: ", file_2_hash(file_2))
    print()

    directory_names, directory_hash = directory_2_hash(directory_1)
    
    local_dict = file_hash_DICT(directory_names, directory_hash)

    for i in directory_names:
	    print("File: ", i, "\t Hash: ", local_dict[i])

    return 0

if __name__ == "__main__":
    main()
