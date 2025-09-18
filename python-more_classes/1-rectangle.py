#!/usr/bin/python3

"""
1-rectangle.py
Define a rectangle
Return: Void
"""


class Rectangle:
    """
    Define a rectangle
    """
    def __init__(self, width: int = 0, height: int = 0):
        """
        __init__ - Init new rectangle
        @width: Width of the rectangle
        @height: Height of the rectangle
        Return: Void
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        width - Get the width of the rectangle
        Return: int - Width value
        """
        return self.__width

    @width.setter
    def width(self, value: int):
        """
        width - Set the width of the rectangle
        @value: Value of the width
        Return: Void
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height - Get the height of the rectangle
        Return: int - Height value
        """
        return self.__height

    @height.setter
    def height(self, value: int):
        """
        height - Set the height of the rectangle
        @value: Value of the height
        Return: Void
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
