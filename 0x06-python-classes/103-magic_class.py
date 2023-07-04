#!/usr/bin/python3
"""This script defines a MagicClass class"""
import math


class MagicClass:
    """
    A class that represents properties of MagicClass.

    Attributes:
        radius: radius.
    """
    def __init__(self, radius=0):
        """Creates a new instance of the MagicClass class.

        Args:
            radius: radius.

        Raises:
            TypeError: radius must be a number .
        """
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Returns the area.

        Returns: area.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
       """Returns the circumference.

        Returns: circumference.
        """

        return 2 * math.pi * self.__radius
