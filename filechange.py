def file_hash_DICT(file_names, file_hashes):
    dict_of_files = {}
    for i in range(len(file_names)):
        dict_of_files[file_names[i]] = file_hashes[i]
    return dict_of_files
    
def assemble_files(directory):
    file_names, file_hashes = directory_2_hash(directory)
    hashed_dir = file_hash_DICT(file_names, file_hashes)
    return (file_names, hashed_dir)