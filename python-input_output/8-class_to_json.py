#!/usr/bin/python3
"""
Module Name: 8-class_to_json.

Contains a function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean) for JSON
serialization of an object.
"""


def class_to_json(obj):
    """Return the dictionary of the class."""
    return obj.__dict__
