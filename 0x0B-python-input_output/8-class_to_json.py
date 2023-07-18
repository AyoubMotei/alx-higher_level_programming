#!/usr/bin/python3
"""
Module for converting an object to a JSON-serializable dictionary.
"""


def class_to_json(obj):
    """
        returns dictionary representation with simple data structure.
    """
    return obj.__dict__
