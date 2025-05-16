#!/usr/bin/python3
"""
Module Name: 3-say_my_name.py

Description:
    This module includes a function to print 'My name is <first name>
    <last name>'

Functions:
    say_my_name(first_name, last_name=""): Prints 'My name is <first
        name> <last name>' and returns None
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name - prints the string 'My name is <first name> <last
        name>'

    Args:
        first_name: string containing my first name.
        last_name: string containing my last name.

    Returns:
        None

    Raises:
        TypeError: if first_name or last_name are not strings
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(f"My name is {first_name} {last_name}")
