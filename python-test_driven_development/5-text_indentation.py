#!/usr/bin/python3
"""
Module Name: 5-text_indentation.py

Description:
    This module includes a function to print 2 new lines after each of these
    characters: '.', '?', and ':' are found in the text.

Functions:
    text_indentation(text): prints the input text with added 2 newlines after
    each appearance of '.', '?' and ':' characters; it returns None
"""


def text_indentation(text):
    """
    text_indentation - prints text with added 2 new lines after '.',
        '?', and ':'

    Args:
        text: text to be printed with modified spacing.

    Returns:
        None

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")
    lines_list = text.split('\n')
    for i in range(len(lines_list)):
        lines_list[i] = lines_list[i].strip()
    text = "\n".join(lines_list)
    print(text, end='')
