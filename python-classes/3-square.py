#!/usr/bin/python3

"""
3-square.py
This module create a square
Return: Void
"""


class Square:
    """
    Define a square
    """
    def __init__(self, size=0):
        """
        __init__ - Init new square
        @size: Size of the square
        Return: Void
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        area - Calculate square area
        Return: int - area value
        """
        return (self._Square__size * self._Square__size)
