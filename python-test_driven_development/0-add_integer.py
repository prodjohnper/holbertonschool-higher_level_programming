#!/usr/bin/python3
''' 
	Function that adds two integers.

	The module includes the `add_integer` function, which can add two integers.
	If only one integer is provided, the function defaults the other to 89.
	It performs type checking to ensure both inputs are valid integers or floats.
	Usage examples:

    >>> add_integer(2, 3)
    5

    >>> add_integer(100, -2)
    98 
'''


def add_integer(a, b=98):
    ''' 
    Adds two integers

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b.
    '''

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
