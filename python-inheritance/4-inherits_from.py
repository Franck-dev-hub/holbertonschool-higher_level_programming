#!/usr/bin/python3

"""
4-inherits_from.py
Check if the object is an instance of a class
that inherited from the specified class
Return: True if it is, else False
"""


def inherits_from(obj, a_class):
    """
    inherits_from - Check if obj inherits from a_class
    @obj: An object
    @a_class: A class
    Return: True if obj inherits from a_class, else False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
