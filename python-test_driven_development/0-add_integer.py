#!/usr/bin/python3
''' 
    Module docstring with 5 lines.

    This module provides a function for adding two integers.

    The `add_integer` function takes two arguments, `a` and `b`,
    which must be integers or floats. If a or b are floats,
    they will be casted before returning the sum.

    Usage examples:

        >>> add_integer(2, 3)
        5

        >>> add_integer(100, -2)
        98
'''


def add_integer(a, b=98):
    '''
    Function docstring with 3 lines.

    Args:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer or float. Defaults to 98.

    Returns:
        int: The sum of a and b.
    '''

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
