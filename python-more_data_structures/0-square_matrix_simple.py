#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_matrix = [_[:] for _ in matrix]
    squared_matrix = list(map(lambda _: list(map(lambda x: x**2, _)), matrix))
    return squared_matrix
