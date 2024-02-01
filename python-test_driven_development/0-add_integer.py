#!/usr/bin/python3
''' Function to add two integers.

	The add_integer function takes two arguments, 'a' and 'b'.

    They're then casted and returned.
'''


def add_integer(a, b=98):
    '''
    Adds two integers.

    Args:
        a (int or float): The Firts number.
        b (int or float): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b.
    '''

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
