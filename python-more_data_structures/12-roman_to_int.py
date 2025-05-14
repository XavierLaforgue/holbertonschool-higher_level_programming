#!/usr/bin/python3
def roman_syntax(roman_string, r_num_rep, r_num_sing, r_dict):
    # No roman character
    if False in [char in r_dict for char in roman_string]:
        return -1
    # Character repeated too many times
    for char in r_num_rep.keys():
        if roman_string.count(char) > 3:
            return -1
    # Repeated nonrepeatable character
    for char in r_num_sing.keys():
        if roman_string.count(char) > 1:
            return -1
    # Substraction with non-substractable character
    if len(roman_string) > 1:
        for i in range(1, len(roman_string)):
            first = r_dict[roman_string[i-1]]
            second = r_dict[roman_string[i]]
            if roman_string[i-1] in r_num_sing and first < second:
                return -1
    # Inapproppriate substraction attempt
    if len(roman_string) > 2:
        for i in range(2, len(roman_string)):
            first = r_dict[roman_string[i-2]]
            second = r_dict[roman_string[i-1]]
            third = r_dict[roman_string[i]]
            if first < third and second <= third:
                return -1
    return 0


def roman_to_int(roman_string):
    if type(roman_string) is not str or len(roman_string) == 0:
        return 0
    r_num_rep = {"I": 1, "X": 10, "C": 100, "M": 1000}
    r_num_sing = {"V": 5, "L": 50,  "D": 500}
    r_dict = r_num_rep | r_num_sing
    roman_string = roman_string.upper()
    roman_syntax_r = roman_syntax(roman_string, r_num_rep, r_num_sing, r_dict)
    if roman_syntax_r != 0:
        return roman_syntax_r
    if len(roman_string) == 1:
        return r_dict[roman_string]
    sum = 0
    first = r_dict[roman_string[0]]
    second = r_dict[roman_string[1]]
    if first >= second:
        sum = sum + first + roman_to_int(roman_string[1:])
    else:
        sum = sum + second - first + roman_to_int(roman_string[2:])
    return sum
