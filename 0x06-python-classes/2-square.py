#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """
    Class that defines properties of a square.

    Attributes:
        __size (int): Size of the square (1 side).
    """

    def __init__(self, size=0):
        """Creates a new instance of the Square class.

        Args:
            size (int): Size of the square (1 side).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

