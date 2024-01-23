#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for nums in range(len(row)):
            if nums == len(row) - 1:
                print('{:d}'.format(nums), end='')
            else:
                print('{:d}'.format(nums), end='')
        print()
