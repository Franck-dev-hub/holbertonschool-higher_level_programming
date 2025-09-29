#!/usr/bin/python3

"""
12-pascal_triangle.py
Print the Pascal triangle
"""


def pascal_triangle(n):
    """
    pascal_triangle - Display Pascal triangle
    @n: Number of triangle lines
    Return: List that image a triangle
    """
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
