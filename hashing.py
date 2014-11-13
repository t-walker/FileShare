__author__ = 'Tyler'

import logging
from hashlib import md5
from os import listdir

logging.basicConfig(filename="hashing.log", level=logging.DEBUG)


def file_2_hash(file):
    """
    @type file: file
    :rtype: md5 object
    """
    file_hash = md5()
    file_hash.update(open(file, 'rb').read())
    file_hash.update(file.encode('UTF-8'))

    return file_hash.hexdigest()


def directory_2_hash(path):
    """
    :param path:
    @type path: string
    :rtype: list
    """
    file_directory = []
    hashed_directory = []

    raw_directory = listdir(path)
    raw_directory.sort()

    for file in raw_directory:
        try:
            hashed_directory.append(file_2_hash(file))
            file_directory.append(file)
        except PermissionError:
            logging.info("[WARNING] ERROR: Cannot access: " + file)
        except IsADirectoryError:
            logging.info("[WARNING] ERROR: Directory: " + file)
            
    return file_directory, hashed_directory
