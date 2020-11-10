"""
    Searches deep inside a directory structure, looking for duplicate file.
    Duplicates aka copies have the same content, but not necessarily the same name.
"""
__author__ = ""
__email__ = ""
__version__ = "1.0"

# noinspection PyUnresolvedReferences
from os.path import getsize, join
from time import time

# noinspection PyUnresolvedReferences
from p1utils import all_files, compare

file_list = all_files('images')
x = 0
def search(file_list):
    lol = []
    while 0 < len(file_list):
        duplicates = [file_list.pop(0)]
        for i in range(len(file_list) - 1, -1, -1):
            if compare(duplicates[0], file_list[i]):
                duplicates.append(file_list.pop(i))
        if 1 < len(duplicates):
            lol.append(duplicates)
    return lol

def report(lol):

    print("== == Duplicate File Finder Report == ==")
    print('File with most duplicates:')
    print (max(lol, key=max))




if __name__ == '__main__':
    path = join(".", "images")

    # measure how long the search and reporting takes:
    t0 = time()
    report(search(all_files(path)))
    print(f"Runtime: {time() - t0:.2f} seconds")

