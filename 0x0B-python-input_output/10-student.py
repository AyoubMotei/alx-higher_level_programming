#!/usr/bin/python3
"""
    Module for the Student class.
"""


class Student:
    """
         A class that represents a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        __init__ : Initializes a Student instance.
        to_json : Retrieves a dictionary representation of the Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the provided attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attr (list): A list of attribute names to retrieve. Default is None.

        Returns:
            dict: A dictionary representation of the Student instance.
        """

        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__
