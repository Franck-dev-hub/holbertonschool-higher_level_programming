#!/usr/bin/python3

"""
2-is_same_class.py
Check if an object is the same of an instance of specified class
Return: True if it is, else False
"""


def is_same_class(obj, a_class):
    """
    is_same_class - Check if obj is the same as a_class
    @obj: An object
    @a_class: A class
    Return: True if obj == a_class, else False
    """
    return type(obj) is a_class
