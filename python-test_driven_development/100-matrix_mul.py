#!/usr/bin/python3

"""
100-matrix_mul.py
This module multiply two matrices
Return: A matrix
"""


def matrix_mul(m_a, m_b):
    """
    matrix_mul - Multiply two matrices
    @m_a: First matrix
    @m_b: Second matrix
    Return: Multiplied matrix
    """

    errors(m_a, m_b)

    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            product = 0
            for k in range(len(m_b)):
                product += m_a[i][k] * m_b[k][j]
            new_row.append(product)
        result.append(new_row)
    return result


def errors(m_a, m_b):
    """
    errors - Manage errors
    @m_a: First matrix
    @m_b: Second matrix
    Return: Void
    """

    # Is a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Is not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    length_row_a = len(m_a[0])
    for row in m_a:
        # Is a list of list
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of list")
        # Is int or float
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        # Rows have the same size
        if len(row) != length_row_a:
            raise TypeError("each row of m_a must be of the same size")

    length_row_b = len(m_b[0])
    for row in m_b:
        # Is a list of list
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of list")
        # Is int or float
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        # Rows have the same size
        if len(row) != length_row_b:
            raise TypeError("each row of m_b must be of the same size")

    # Can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
