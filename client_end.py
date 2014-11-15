def assemble_files(directory):
    file_names, file_hashes = directory_2_hash(directory)
    hashed_dir = file_hash_DICT(file_names, file_hashes)
    return (file_names, hashed_dir)