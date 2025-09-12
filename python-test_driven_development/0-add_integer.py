#!/usr/bin/python3

"""
0-add_integer.py
This module add two integers or floats
Return int
"""


def add_integer(a, b=98):
    """
    This function add two integers or floats
    Floats are casted to integers before addition
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return int(a + b)
