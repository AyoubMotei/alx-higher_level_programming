#!/usr/bin/python3
def read_file(filename=""):
    """ Function that reads a text file encoded in UTF-8 and prints its contents to the standard output. """

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
