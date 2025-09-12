#!/usr/bin/python3

import numpy as np

"""
101-lazy_matrix_mul.py
This module multiply two matrices with numpy
"""

def lazy_matrix_mul(m_a, m_b):
    """
    lazy_matrix_mul - Multiply two matrices with numpy
    @m_a: First matrix
    @m_b: Second matrix
    Return: Multiplied matrix
    """

    errors(m_a, m_b)

    try:
        return np.matmul(m_a, m_b)
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")


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

    # Is a list of list
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list)for row in m_b):
        raise TypeError("m_b must be a list of lists")

    length_row_a = len(m_a[0])
    for row in m_a:
        # Is int or float
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError("m_a should contain only integers or floats")
        # Rows have the same size
        if len(row) != length_row_a:
            raise TypeError("each row of m_a must be of the same size")

    length_row_b = len(m_b[0])
    for row in m_b:
        # Is int or float
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError("m_b should contain only integers or floats")
        # Rows have the same size
        if len(row) != length_row_b:
            raise TypeError("each row of m_b must be of the same size")
