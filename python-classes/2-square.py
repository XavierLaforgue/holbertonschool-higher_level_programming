#!/usr/bin/python3
"""
Module Name: 1-square.py

Contains only one class to define an object named square and
characterize it with its size

Classes:
    Square - defines a square and size as one of its attributes
"""


class Square(object):
    """
    Creates a Square class of objects which is defined with a size.

    Attributes:
        size - private attribute for the square.
    """
    def __init__(self, size=0):
        """
        Initialize instance of square with optional size argument.

        Args:
            size - int
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise TypeError('size must be >= 0')
        self.__size = size
