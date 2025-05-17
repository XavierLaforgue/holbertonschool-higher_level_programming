#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    keys = [k for k, v in a_dictionary.items() if v == value]
    [a_dictionary.pop(k) for k in keys]
    return a_dictionary
