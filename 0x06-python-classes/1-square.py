#!/usr/bin/python3
"""This code defines a class called Square"""


class Square:
    """
    This class defines the properties of a square. It is based on the code from the 0-square.py file..

    Attributes:
        size: The size attribute represents the length of a side of the square.
    """
    def __init__(self, size):
        """The init method initializes new instances of the Square class. It takes a size parameter representing the size of the square.

        Args:
            size: The size parameter represents the size of the square.
        """
        self.__size = size

