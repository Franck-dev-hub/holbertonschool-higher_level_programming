#!/usr/bin/python3

"""
0-lookup.py
Return a list of avaiable attributes ans methods of an object
Return: A list object
"""


def lookup(obj):
    """
    Look object attributes & methods
    Return: A list object
    """
    return dir(obj)
