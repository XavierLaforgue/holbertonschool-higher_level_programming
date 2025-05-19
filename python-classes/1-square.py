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
    def __init__(self, size):
        """
        Initialize instance of square
        """
        self.__size = size
