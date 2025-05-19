#!/usr/bin/python3
"""
Module Name: 1-square.py

Contains only one class to define an object named square

Classes:
    Square - defines a square and instantiates size as an optional
        private attribute. It accepts only positive integers as size.
        Property getter and setter are made available for size.
        Offers public method area to return the area of the square.
        Offers public method my_print to print the square to stdout.
"""


class Square(object):
    """
    Creates a Square class of objects which is defined with a size and
    offers getter and setter methods for that property; also makes
    available the methods area and my_print.

    Attributes:
        size - private attribute for the Square. it is a positive
            integer.

    Methods:
        size - with an argument sets that value to the size attribute,
            without it it returns the value of the size attribute.
        area - returns the area of the Square.
        my_print - prints the square to the standard output using the
            character #
    """

    def __init__(self, size: int = 0):
        """
        Initializes instance of Square with optional size argument
        using the size property setter.

        Args:
            size - a positive integer.
        """
        self.__size = size

    @property
    def size(self) -> int:
        """
        Property getter for size. Retrieves the value of Square's size.

        Returns:
            size of Square, positive integer.
        """
        return self.__size

    @size.setter
    def size(self, value) -> None:
        """
        Property setter for size. Sets the value of Square's size.

        Raises:
            TypeError: if value is not integer
            ValueError: if value is negative
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self) -> int:
        """
        Calculates the area of the Square.

        Returns:
            area of the Square, an integer.
        """
        return self.__size**2

    def my_print(self) -> None:
        """
        Prints the square to stdout using #
        """
        for i in range(self.size):
            print("#"*self.size)
        if not self.size:
            print()
