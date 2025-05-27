#!/usr/bin/python3
"""
Module Name: task_01_duck_typing.

Contains an abstract class Shape and subclasses Circle and Rectangle
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Define a Shape."""

    @abstractmethod
    def area(self) -> float:
        """Define area of Shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Define perimeter of Shape."""
        pass


class Circle(Shape):
    """Define the Circle Shape."""

    def __init__(self, radius):
        """Initialize Circle with its radius."""
        self.__radius = abs(radius)

    def area(self):
        """Define the area of a Circle."""
        return pi * self.__radius ** 2

    def perimeter(self):
        """Define the perimeter of a Circle."""
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """Define the Rectangle Shape."""

    def __init__(self, width, height):
        """Intialize Rectangle with its width and height."""
        self.__width = width
        self.__height = height

    def area(self):
        """Define the area of a Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Define the perimeer of a Rectangle."""
        return 2 * (self.__width + self.__height)


def shape_info(shape_obj):
    """Print shape information.

    Args:
        shape_obj (obj): shape object whose information will be
            printed.

    Examples:
    >>> circle = Circle(1)
    >>> shape_info(circle) # doctest: +ELLIPSIS
    Area: 3.141592...
    Perimeter: 6.2831...
    >>> rectangle = Rectangle(2, 3)
    >>> shape_info(rectangle)
    Area: 6
    Perimeter: 10
    """
    print(f"Area: {shape_obj.area()}")
    print(f"Perimeter: {shape_obj.perimeter()}")


if __name__ == "__main__":
    circle = Circle(1)
    rectangle = Rectangle(2, 3)
    shape_info(circle)
    shape_info(rectangle)
