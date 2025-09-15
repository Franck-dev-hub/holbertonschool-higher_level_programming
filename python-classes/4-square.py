#!/usr/bin/python3

"""
4-square.py
This module create a square
Return: Void
"""


class Square:
    """
    Define a square
    """
    def __init__(self, size: int = 0):
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

    @property
    def size(self):
        """
        size - Get size of the square
        Return: int - Size of the square
        """
        return self.__size

    @size.setter
    def size(self, value: int):
        """
        size - Set the size of the square
        @value: Value of the size
        Return: Void
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
