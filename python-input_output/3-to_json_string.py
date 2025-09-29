#!/usr/bin/python3

"""
3-to_json_string.py
Get json informations
"""

import json


def to_json_string(my_obj):
    """
    to_json_string - Create a json from an object
    @my_obj: Object to parse
    Return: Json representation
    """
    return json.dumps(my_obj)
