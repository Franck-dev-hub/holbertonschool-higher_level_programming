#!/usr/bin/python3

"""
4-rectangle.py
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

    def __str__(self):
        """
        __str__ - Return human readable str
        Return: str - Result
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        result = ""

        for char in range(self.__height):
            result += "#" * self.__width
            if char != self.__height - 1:
                result += "\n"
        return result

    def __repr__(self):
        """
        __repr__ - Return debug representation of the rectangle
        Return: str - Result
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    @property
    def width(self):
        """
        width - Get the width of the rectangle
        Return: int - Width value
        """
        return self.__width

    @width.setter
    def width(self, value: int):
        """Calculate the area of the rectangle
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

    def area(self):
        """
        area - Calculate the area of the rectangle
        Return: int - The area of the rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        perimeter - Calculate the perimeter of the rectangle
        Return: int - The perimeter of the rectangle
        """
        if self.__height == 0 or self.width == 0:
            return 0
        return ((self.__height + self.__width) * 2)
