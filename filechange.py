def file_hash_DICT(file_names, file_hashes):
    dict_of_files = {}
    for i in range(len(file_names)):
        dict_of_files[files_names[i]] = file_hashes[i]
    return dict_of_files
    
    