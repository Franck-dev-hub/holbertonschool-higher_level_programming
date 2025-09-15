#!/usr/bin/python3

"""
102-square.py
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

    def __eq__(self, other: int):
        """
        __eq__ - Check if 2 squares are equal
        @other: The other square
        Return: True if equal, False if not
        """
        return self.area() == other.area()

    def __ne__(self, other: int):
        """
        __ne__ - Check if 2 squares are not equal
        @other: The other square
        Return: True if not equal, False if it is
        """
        return self.area() != other.area()

    def __gt__(self, other: int):
        """
        __gt__ - Check if first square is greater than the other
        @other: The other square
        Return: True if greater, False if not
        """
        return self.area() > other.area()

    def __ge__(self, other: int):
        """
        __ge__ - Check if first square is greater or equal to the other
        @other: The other square
        Return: True if greater or equal, False if not
        """
        return self.area() >= other.area()

    def __lt__(self, other: int):
        """
        __lt__ - Check if first square is less than the other
        @other: The other square
        Return: True if less, False if not
        """
        return self.area() < other.area()

    def __le__(self, other: int):
        """
        __le__ - Check if first square is less or equal to the other
        @other: The other square
        Return: True if less or equal, False if not
        """
        return self.area() <= other.area()
