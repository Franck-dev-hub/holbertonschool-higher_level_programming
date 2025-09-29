#!/usr/bin/python3

import json

"""
5-save_to_json_file.py
Save an object in a json file
"""

def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - Write in a json file
    @my_obj: Object to write in json file
    @filename: Name of json file
    Return: Void
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
