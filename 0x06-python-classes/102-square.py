#!/usr/bin/python3
"""This script defines a Square class"""


class Square:
    """
    A class that represents a square and its properties (based on 3-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """Creates a new instance of the Square class.

        Args:
            size: size of the square (1 side).
        """
        self.__size = size

    def area(self):
        """Calculates the area of the square.

        Returns: the current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): size of a square (1 side).

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __lt__(self, other):
        """Compares the area of the square to determine if it is less than another square.

        Args:
            other (Square): square to compare size to.

        Returns: True or false.
        """
        return self.__size < other.__size

    def __le__(self, other):
        """Compares the area of the square to determine if it is less than or equal to another square.

        Args:
            other (Square): square to compare size to.

        Returns: True or false.
        """
        return self.__size <= other.__size

    def __eq__(self, other):
        """Compares the area of the square to determine if it is equal to another square."

        Args:
            other (Square): square to compare size to.

        Returns: True or false
        """
        return self.__size == other.__size

    def __ne__(self, other):
        """Compares the area of the square to determine if it is not equal to another square.

        Args:
            other (Square): square to compare size to.

        Returns: True or false
        """
        return self.__size != other.__size

    def __gt__(self, other):
        """Compares the area of the square to determine if it is greater than another square.

        Args:
            other (Square): square to compare size to.

        Returns: True or false
        """
        return self.__size > other.__size

    def __ge__(self, other):
        """Rich comparison operator to compare if square area is greater
        than or equal to another.

        Args:
            other (Square): square to compare size to.

        Returns: True or false
        """
        return self.__size >= other.__size
