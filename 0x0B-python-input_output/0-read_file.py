#!/usr/bin/python3
"""
Module: 0-read_file
"""


def read_file(filename=""):
    """
      read_file function reads a text file (UTF8) and prints its content to stdout
    Args:
        filename: name of the file to be read
    """
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
