#!/usr/bin/python3

"""
2-matrix_divided.py
This module divides all elements of a matrix
Return a matrix
"""


def matrix_divided(matrix, div):
    """
    Main divide function
    """
    errors(matrix, div)

    new_matrix = [row.copy() for row in matrix]
    for row in range(len(matrix)):
        for col, num in enumerate(matrix[row]):
            new_matrix[row][col] = round(num / div, 2)
    return new_matrix


def errors(matrix, div):
    """
    Error management function
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    last_row = matrix[0]
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                    "matrix must be a matrix"
                    " (list of lists) of integers/floats"
                    )
        if len(row) != len(last_row):
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(
                        "matrix must be a matrix"
                        " (list of lists) of integers/floats")
