#!/usr/bin/python3
''' 
	Function that adds two integers.
    
    a and b must be integers or floats, otherwise raise a TypeError exception.
    If a or b are floats, the have to be casted before returning them.
'''


def add_integer(a, b=98):

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
