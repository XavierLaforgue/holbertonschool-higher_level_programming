#!/usr/bin/python3
def no_c(my_string):
    new_string = [char for char in my_string if char.lower() != "c"]
    return "".join(new_string)
    """ new_string = ""
    for char in my_string:
        if char.lower() != "c":
            new_string += char
    return new_string """
