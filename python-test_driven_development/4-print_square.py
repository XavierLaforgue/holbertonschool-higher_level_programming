#!/usr/bin/python3
"""
Module Name: 4-print_square.py

Description:
    This module includes a function to print a square using '#'

Functions:
    print_square(size): prints a square of size 'size' and returns None
"""


def print_square(size):
    """
    print_square - prints a square of size 'size' using '#'

    Args:
        size: size of the sides of the square

    Returns:
        None

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for height in range(size):
        print('#' * size)
