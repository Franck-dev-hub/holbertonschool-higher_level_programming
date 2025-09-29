#!/usr/bin/python3

"""
4-from_json_string.py
Return un object represented by a JSON string
"""

import json


def from_json_string(my_str):
    """
    from_json_string - Create an object from a json
    @my_str: String to parse
    Return: An object
    """
    return json.loads(my_str)
