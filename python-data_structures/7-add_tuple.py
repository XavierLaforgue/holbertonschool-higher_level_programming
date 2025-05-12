#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """ x, y = 0, 0
    if len(tuple_a) > 0:
        x += tuple_a[0]
    if len(tuple_b) > 0:
        x += tuple_b[0]
    if len(tuple_a) > 1:
        y += tuple_a[1]
    if len(tuple_b) > 1:
        y += tuple_b[1] """
    a = tuple_a[0:2]
    b = tuple_b[0:2]
    a += (2 - len(a)) * (0,)
    b += (2 - len(b)) * (0,)
    x = a[0] + b[0]
    y = a[1] + b[1]
    return x, y
