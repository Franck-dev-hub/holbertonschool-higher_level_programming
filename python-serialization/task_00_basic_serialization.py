#!/usr/bin/python3

"""
task_00_basic_serialization.py
Serialize, save, load datas to & from a file
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    serialize_and_save_to_file - Serialize and save to a file
    @data: A Python Dictionary with data
    @filename: The filename of the output JSON file.
    Return: Void
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    load_and_deserialize - Load and deserialize data from a file
    @filename: The filename of the input JSON file
    Return: Dictionary with desialized json data from the file
    """
    with open(filename, 'r', encoding="utf-8") as file:
        obj = json.load(file)

    return obj
