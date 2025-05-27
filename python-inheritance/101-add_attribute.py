#!/usr/bin/python3
"""
Module Name: 101-add_attribute.

Contains a function that adds an attribute to an object if it is
possible.
"""


def add_attribute(obj: object, attr: str, value: str):
    """Add a new attribute to an object.
    
    Args:
        obj (object): object to which an attribute will be added, if
            possible.
        attr (str): name of the attribute that will be added, if
            possible.
        value (str): value that will be assigned to attr, if possible.

    Raises:
        TypeError: if the attribute can not be added.
    """

    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
    