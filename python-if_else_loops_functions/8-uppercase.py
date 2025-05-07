#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            char_up = chr(ord(char) + ord('A') - ord('a'))
        else:
            char_up = char
        print("{}".format(char_up), end="")
    print("")
