#!/usr/bin/python3

"""
4-print_square.py
This module prints a square with the char #
Return Void
"""


def print_square(size):
    """
    print_square - It prints a square with char #
    @size: Size of the square
    Return: Void
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
