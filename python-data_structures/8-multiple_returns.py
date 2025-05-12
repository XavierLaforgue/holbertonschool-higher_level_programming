#!/usr/bin/python3
def multiple_returns(sentence):
    strlen = len(sentence)
    if strlen == 0:
        first = None
    else:
        first = sentence[0]
    return strlen, first
