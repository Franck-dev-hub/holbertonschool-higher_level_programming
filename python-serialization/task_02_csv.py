#!/usr/bin/python3

"""
task_02_csv.py
Convert csv to json
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    convert_csv_to_json - Convert csv data to json format
    @filename: Name of the file
    Return: True if success, else False
    """
    try:
        with open(filename, newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = list(reader)

        with open("data.json", 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        return True
    except FileNotFoundError:
        return False
