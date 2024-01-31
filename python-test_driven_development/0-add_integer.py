#!/usr/bin/python3
''' Function that adds two integers. '''


def add_integer(a, b=89):
    ''' Adds two integers

    Args:
            a (int or float): The first number.
            b (int or float): The second number. Defaults to 89.

    Returns:
            int: The sum of a and b.

    Raises:
            TypeError: If a or b is not an integer or float.
    '''

    a = int(a) if isinstance(a, (int, float)) else None
    b = int(b) if isinstance(b, (int, float)) else None

    if not isinstance(a, int):
        raise TypeError('a must be an integer')
    if not isinstance(b, int):
        raise TypeError('b must be an integer')

    return a + b
