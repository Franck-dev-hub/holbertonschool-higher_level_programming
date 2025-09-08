#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    new_matrix = matrix.copy()

    return list(map(lambda y: list(map(lambda x: x * x, y)), new_matrix))
