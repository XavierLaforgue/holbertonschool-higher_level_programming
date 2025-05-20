#!/usr/bin/python3
"""
Module name: 2-rectangle.py

Contains a class Rectangle that defines a rectangle by its width and
height and offers methods to obtain its area and perimeter.

Classes:
    Rectangle: defines a rectangle by its width and height, makes area
    and perimeter methods available.
"""


class Rectangle(object):
    """
    Creates a class Rectangle that defines a rectangle by private instance
    attributes width and height, and methods area and perimeter.
    """
    def __init__(self, width: int = 0, height: int = 0) -> None:
        """
        Initializes Rectangle object.
        The created instance takes two optional arguments, each wich
        may be set to the corresponding private attribute via its
        property setter.
        """
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """
        Getter for the width private instance attribute
        """
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        """
        Setter for the width private attribute.
        It ensures the input value for width is a positive integer before
        assigning it to the instance attribute, it raises errors if unesired
        input.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self) -> int:
        """
        Getter for the height private instance attribute
        """
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        """
        Setter for the height private attribute.
        It ensures the input value for height is a positive integer before
        assigning it to the instance attribute, it raises errors if unesired
        input.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self) -> int:
        """
        Calculates and returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self) -> int:
        """
        Calculates and returns the perimeter of the rectangle.
        """
        if not self.width or not self.height:
            return 0
        return 2 * (self.width + self.height)
