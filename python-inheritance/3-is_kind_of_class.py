#!/usr/bin/python3

"""
3-is_kind_of_class.py
Check if the object is an instance of or
if the object is an instance of a class that inherited from the specified class
Return: True if it is, else False
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class - Compare obj and class
    @obj: An object
    @a_class: A class
    Return: True if obj == a_class, else False
    """
    return isinstance(obj, a_class)
