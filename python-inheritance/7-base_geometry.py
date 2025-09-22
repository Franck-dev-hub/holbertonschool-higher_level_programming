#!/usr/bin/python3

"""
7-base_geometry.py
Class 'BaseGeometry'
Return Error
"""


class BaseGeometry():
    """
    BaseGeometry - A class
    Return: Void
    """
    def area(self):
        """
        area - Not implemented
        Return: Error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        interger_validator - Check if value is int > 0
        @name: A string
        @value: An int to check
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
