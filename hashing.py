__author__ = 'Tyler'

from hashlib import md5
from os import listdir

def file_2_hash(file):
    return md5(open(file).read()).hexdigest()

def directory_2_hash(path):
    """
    @type path: string
    :rtype: list
    """

    hashed_directory = []

    for file in listdir(path):
        hashed_directory.append(file_2_hash(file))

    return hashed_directory