#!/usr/bin/python3
"""
Module Name: task_01_pickle.

Contain a custom class with a few methods including one to pickle
itself.
"""
import pickle
import os


class CustomObject(object):
    """Define a Custom Object."""

    def __init__(self, name: str, age: int, is_student: bool):
        """Instantiate Custom Object with attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the attributes of the custom object."""
        try:
            print(f"Name: {self.name}\nAge: {self.age}\n"
                  f"Is Student: {self.is_student}")
        except Exception:
            pass
        
    def serialize(self, filename: str):
        """Serialize class into file using picle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            pass

    @classmethod
    def deserialize(cls, filename: str) -> "CustomObject | None":
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                loaded = pickle.load(f)
            if isinstance(loaded, CustomObject):
                return loaded
        return None
