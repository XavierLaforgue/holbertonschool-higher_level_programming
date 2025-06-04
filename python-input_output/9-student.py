#!/usr/bin/python3
"""
Module Name: 9-student.

Contains the definition of a class Student.
"""


class Student(object):
    """Define a student."""

    def __init__(self, first_name, last_name, age):
        """Instantiate with public attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary representation of a Student instance."""
        return self.__dict__
