#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {k: 2*a_dictionary[k] for k in a_dictionary.keys()}
