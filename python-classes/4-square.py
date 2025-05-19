#!/usr/bin/python3
"""
Module Name: 1-square.py

Contains only one class to define an object named square

Classes:
    Square - defines a square and instantiates size as a private attribute.
        It accepts only positive integers as size.
        Offers public method area to return the area of the square.
"""


class Square(object):
    """
    Creates a Square class of objects which is defined with a size and
    offers the method area.

    Attributes:
        size - private attribute for the Square, positive integer.

    Methods:
        area - reaturns the area of the Square.
    """
    def __init__(self, size=0):
        """
        Initializes instance of Square with optional size argument.

        Args:
            size - positive int

        Raises:
            TypeError: if size is not an int
            ValueError: if size is negative
        """
        self.__size = size

    def area(self):
        """
        Calculates the area of the Square.

        Returns:
            area of the Square, an int.
        """
        return self.__size**2

    @property
    def size(self):
        """
        Property getter for size. Retrieves the value of Square's size.

        Returns:
            size of Square, int.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Property setter for size. Sets the value of Square's size.

        Returns:
            None

        Raises:
            TypeError: if value is not int
            ValueError: if value is negative
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
