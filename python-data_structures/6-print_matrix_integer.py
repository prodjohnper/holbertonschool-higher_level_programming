#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for _ in matrix:
        print(''.join('{:d}'.format(row) for row in _))
