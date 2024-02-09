#!/usr/bin/python3
'''
    12-pasccal_triangle.py
    Description: Create a function def pascal_triangle(n): that returns
    a list of lists of integers representing the Pascal's triangle of n
'''


def pascal_triangle(n):
    ''' Function that returns a list of lists of
        integers representing the Pascal's triangle of n
    '''
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        row = [1] + [triangle[-1][i] + triangle[-1][i + 1]
                     for i in range(len(triangle[-1]) - 1)] + [1]
        triangle.append(row)
    return triangle
