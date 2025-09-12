#!/usr/bin/python3

"""
3-say_my_name.py
This module prints the first name and the last name
Return: Void
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name - Print first_name & last_name
    @first_name: First name like "John"
    @last_name: Last name like "Doe"
    Return: Void
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
