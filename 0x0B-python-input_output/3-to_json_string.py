#!/usr/bin/python3
"""
Module for converting an object to a JSON string.
"""

def to_json_string(my_obj):
    """Returns the JSON representation of an object as a string."""
    return json.dumps(my_obj)
