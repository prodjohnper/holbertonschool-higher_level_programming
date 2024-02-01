#!/usr/bin/python3
''' Function to add two integers.

    They're then casted and returned.

'''


def add_integer(a, b=98):
    ''' Adds two integers.
        Returns: The sum of a and b.
    '''
    error_msg = "unsupported operand type(s) for +: 'NoneType' and 'int'"
    if a is None or b is None:
        raise TypeError(error_msg)

    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be and integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be and integer')

    return int(a) + int(b)
