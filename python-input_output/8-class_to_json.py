#!/usr/bin/python3

"""
8-class_to_json.py
Create a dictionary description from an object
"""


def class_to_json(obj):
    """
    class_to_json - Create a dict description from an object
    @obj: Object to parse
    Return: Dict object
    """
    return obj.__dict__
