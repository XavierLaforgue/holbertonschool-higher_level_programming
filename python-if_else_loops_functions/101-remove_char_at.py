#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    for i in range(0, len(str)):
        if i != n:
            str2 += str[i]
        else:
            str2 += ""
    return str2
