#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for a, b in sorted(a_dictionary.items()):
        print("{}: {}".format(a, b))
    # sorting key-value pairs by key and by value if keys ar the same
    # also capital and lower case letters are considered to be equivalent:
    """
    for i in sorted(
            {"a": 2, "d": 4, "h": 4, "B": 5, "p": 1000, "c": 3}.items(),
            key=lambda kv: (kv[0].lower(), kv[1])):
        print(i)
    """
