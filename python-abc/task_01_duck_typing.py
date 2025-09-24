#!/usr/bin/python3

"""
task_01_duck_typing.py
Define an abstract method
Return a string
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Shape - Shape class
    """
    @abstractmethod
    def area(self):
        """
        area - area abstract function
        Return: Void
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        perimeter - perimeter abstract function
        Return: Void
        """
        pass


class Circle(Shape):
    """
    Circle - Circle class
    """
    def __init__(self, radius):
        """
        __init__ - Init function
        @radius: Radius
        Return: Void
        """
        self.__radius = radius

    def area(self):
        """
        area - Area function
        Return: Circle area
        """
        return (pi * self.__radius * self.__radius)

    def perimeter(self):
        """
        perimeter - Perimeter function
        Return: Circle perimeter
        """
        return (2 * pr * self.__radius)


class Rectangle(Shape):
    """
    Rectangle - Rectangle class
    """
    def __init__(self, width, height):
        """
        __init__ - Init function
        @width: Width of the rectangle
        @height: Height of the rectangle
        Return: Void
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        area - Area function
        Return: Rectangle area
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        perimeter - Perimeter function
        Return: Rectangle perimeter
        """
        return ((self.__width + self.height) * 2)


def shape_info(obj):
    """
    shape_info - Shape informations
    @obj: Target object to display informations
    Return: Void
    """
    area = obj.area()
    perimeter = obj.permiter()
    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))
