#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dict = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    prev_value = 0
    result = 0

    if not isinstance(roman_string, str):
        return result

    for _ in roman_string:
        value = roman_dict.get(_, 0)
        if value == 0:
            return 0
        if 0 < prev_value < value:
            result += value - prev_value * 2
        else:
            prev_value = value
            result += value
    return result
