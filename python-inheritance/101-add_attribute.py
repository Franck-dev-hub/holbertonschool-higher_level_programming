#!/usr/bin/python3

"""
101-add_attribute.py
Add a new attribute to an object if it's possbile
"""


def add_attribute(self, key, value):
    """
    add_attribute - Add an attribute if it's possible
    @key: Key of the object
    @value: Value of the object
    Return: Void
    """
    if not hasattr(self, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(self, key, value)
