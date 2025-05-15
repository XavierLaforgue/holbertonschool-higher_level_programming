#!/usr/bin/python3
"""
This module's purpose is to contain only one function.

Function(s): add_integer

With this function we can add two integers or add an integer to 98.
It raises a Type Exception if at least one of the arguments is not
an int or a float.
Floats are casted (truncated) to integers without raising an Exception.
"""


def add_integer(a, b=98):
    """
    add_integer - Returns the integer addition of two numbers.

    For integer inputs it performs straightforwardly:
    >>> add_integer(2, 3)
    5

    Float inputs are converted to integers before performing the
    operation as usual:
    >>> add_integer(4.5, 10)
    14

    The second input is 98 by default:
    >>> add_integer(2)
    100

    Non-integer and non-float input raises a TypeError exception:
    >>> add_integer('hello', 3)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer
    >>> add_integer(10, 'world')
    Traceback (most recent call last):
    ...
    TypeError: b must be an integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
