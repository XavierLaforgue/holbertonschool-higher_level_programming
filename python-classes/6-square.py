#!/usr/bin/python3
"""
Module Name: 6-square.py

Contains only one class to define an object named square.

Classes:
    Square - defines a square and instantiates size and positon as
        optional private attributes. It accepts only positive integers
        as size and a tuple of 2 positive integers as position.
        Getter and setter are made available for size and position.
        Offers public method area to return the area of the square.
        Offers public method my_print to print the square to stdout.
"""


class Square(object):
    """
    Creates a Square class of objects defined with a size and a
    position, both with getter and setter methods available; also makes
    available the methods area and my_print.

    Attributes:
        size - private attribute for the Square. it is a positive
            integer. Optional at instantiation.
        position - private attribute for the Square, it is a tuple of 2
            positive integers.

    Methods:
        size - property setter and getter. if an argument is passed or
            if an assignment is made to it, it sets the passed value to
            the size attribute, without it it returns the value of the
            size attribute.
        position - property setter and getter. If an argument is passed or
            if an assignment is made to it, it sets the passed value to
            the position attribute, without it it returns the value of the
            position attribute.
        area - returns the area of the Square.
        my_print - prints the square to the standard output using the
            character #
    """

    def __init__(self, size: int = 0,
                 position: tuple[int, int] = (0, 0)):
        """
        Initializes instance of Square with optional size and position
        arguments using the corresponding property setters. Both are private
        instance attributes.

        Args:
            size - a positive integer.
            position - a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self) -> tuple[int, int]:
        """
        Property getter for position. Retrieves the Square's position.

        Returns:
            position of the Square, tuple of two positive inntegers.
        """
        return self.__position

    @position.setter
    def position(self, value) -> None:
        """
        Property setter for position. Sets the value of Square's
        position.

        Raises:
            TypeError: if not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                not all(isinstance(elem, int) for elem in value) or
                any(map(lambda x: x < 0, value))):
            raise TypeError('position must be a tuple of 2 positive '
                            'integers')
        self.__position = value

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
        print("\n"*self.position[1], end="")
        for i in range(self.size):
            print(" "*self.position[0], end="")
            print("#"*self.size)
        if not self.size:
            print()
