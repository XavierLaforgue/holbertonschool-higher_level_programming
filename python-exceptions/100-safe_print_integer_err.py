#!/usr/bin/python3
"""
Module Name: 100-safe_print_integer_err.py

Dependency: sys

Description: contains one function to print an integer.

Function(s): safe_print_integer_err - prints an integer, returns
    True if the value was printed (i.e., it was an integer), prints
    to the standard error if an exception was produced.
"""

import sys


def safe_print_integer_err(value):
    """
    safe_print_integer_err - prints an integer

    Description:
        Prints a value if it is an integer. Safely handle the case when the
        input is not an integer and print to the standard error.

    Arg(s):
        value - integer to be printed

    Returns:
        True if the value was printed (i.e., it was an integer),
            False otherwise

    Raise:
           TypeError: if value is not an int
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
