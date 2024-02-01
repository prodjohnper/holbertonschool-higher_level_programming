#!/usr/bin/python3
''' Function to add two integers.

    They're then casted and returned.
    
'''


def add_integer(a, b=98):
    ''' Adds two integers.

        Returns: The sum of a and b.

    '''

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
