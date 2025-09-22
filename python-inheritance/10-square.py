#!/usr/bin/python3

"""
10-square.py
Define Square that inherits from Rectangle
Return: Void
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square - Set a square object
    Return: Void
    """
    def __init__(self, size):
        """
        __init__ - Init function
        @size: Size of the square
        Return: Void
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        __str__ - Human readable output
        Return: String
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        area - Calculate the area of the square
        Return: int - the area of the square
        """
        return (self.__size * self.__size)
