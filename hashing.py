__author__ = 'Tyler'

from hashlib import md5
from os import listdir


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
    hashed_directory = []

    for file in listdir(path):
        try:
            hashed_directory.append(file_2_hash(file))
        except PermissionError:
            print("[-] ERROR: Cannot access:", file)
    return hashed_directory
