#!/usr/bin/python3
"""
Module Name: 100-append_after.

Contains a function that inserts a line of text to a file after each
line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Append a line of text to a file."""
    with open(filename, "r", encoding="utf-8") as f:
        file_lines = f.readlines()
    with open(filename, "w", encoding="utf-8") as f:
        for line in file_lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)


if __name__ == "__main__":
    append_after("append_after_100.txt", "is", "\"C is fun!\"\n")
