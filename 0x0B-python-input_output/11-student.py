#!/usr/bin/python3
'''Module for the Student class.'''


class Student:
    '''A class representing a student with JSON functionality.'''
    def __init__(self, first_name, last_name, age):
        '''Constructor for the Student class.'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves a dictionary representation of the Student instance with optional attribute filtering.'''
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        '''Updates the attributes of the Student instance using a dictionary.'''
        for key, value in json.items():
            self.__dict__[key] = value
