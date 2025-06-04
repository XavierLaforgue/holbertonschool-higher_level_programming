#!/usr/bin/python3
"""
Module Name: 11-student.

Contains the definition of a class Student.
"""


class Student(object):
    """Define a student.

    Args:
        first_name (str): first name of the student.
        last_name (str): last ame of the student.
        age (int): age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """Instantiate with public attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of a Student instance.

        Args:
            attrs (optional, list[str]): list of attributes to choose
                the dictionary elements that will be kept.
        """
        if (isinstance(attrs, list)
                and all(isinstance(attr, str) for attr in attrs)):
            my_dict = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    my_dict.update({k: v})
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Recover dictionary representation of a Student instance.

        Args:
            json (dict): dictionary with the attributes with which to
            reload the Student instance.
        """
        json.setdefault("age", 1)
        json.setdefault("first_name", "J")
        json.setdefault("last_name", "S")
        self.last_name = json.get("last_name")
        self.first_name = json.get("first_name")
        self.age = json.get("age")
