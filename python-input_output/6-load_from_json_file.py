#!/usr/bin/python3

"""
6-load_from_file.py
Create un object from a json file
"""

import json


def load_from_json_file(filename):
    """
    load_from_json_file - Load datas from a json file
    @filename: Name of the file
    Return: Object from json
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.loads(file.read())
