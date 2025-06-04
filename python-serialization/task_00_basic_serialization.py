#!/usr/bin/python3
"""
Module Name: task_00_basic_serialization.

Contains two functions. One to serialize a Python dictionary to JSON
and another to deserialize the JSON file to recreate the Python
dictionary.
"""

import json
def serialize_and_save_to_file(data: dict, filename: str):
    """Serialize and save dictionary to JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename: str):
    """Load and deserialize JSON file to original object."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
