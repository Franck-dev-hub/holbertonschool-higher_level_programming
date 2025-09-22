#!/usr/bin/python3

"""
100-my_int.py
Invert == and != values
"""


class MyInt(int):
    """
    MyInt - Custom int
    """
    def __eq__(self, value):
        """
        __eq__ - Invert == operator
        @value: Value to be checked
        Return: self != value
        """
        return int(self) != value

    def __ne__(self, value):
        """
        __ne__ - Invert != operator
        @value: Value to be checked
        Return: self == value
        """
        return int(self) == value
