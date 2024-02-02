#!/usr/bin/python3
"""
	4-print_square.py

	Function that prints a square with the character #.
"""


def print_square(size):
    """ Description: prints a square with the character #
        size is the size length of the square
    """

    err = "unsupported operand type(s) for +: 'NoneType' and 'int'"

    if size is None:
        raise TypeError(err)

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and type(size) < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print('#' * size)
