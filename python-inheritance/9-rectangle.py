#!/usr/bin/python3

"""
9-rectangle.py
Define Rectangle that inherits from BaseGeometry
Return: Void
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle - Set a rectangle object
    Return: Void
    """
    def __init__(self, width, height):
        """
        __init__ - Init function
        @width: Width value
        @height: Height value
        Return: Void
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def __str__(self):
        """
        __str__ - Human readable output
        Return: String
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        area - Calculate the area of the recangle
        Return: int - the area of the rectangle
        """
        return (self.__width * self.__height)
