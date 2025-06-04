#!/usr/bin/python3
"""
Module Name: 10-student.

Contains the definition of a class Student.
"""


class Student(object):
    """Define a student."""

    def __init__(self, first_name, last_name, age):
        """Instantiate with public attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for k, v in self.__dict__.items():
            if k in attrs:
                my_dict.update({k: v})
        return my_dict
