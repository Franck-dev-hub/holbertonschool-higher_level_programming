#!/usr/bin/python3

"""
7-add_item.py
Adds all arguments to a python list and save them to a file
"""

import sys
import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    """
    main - Main function to merge all arguments
    """
    if len(sys.argv) < 2:
        my_list = []

    filename = "add_item.json"
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []

    for arg in range(1, len(sys.argv)):
        my_list.append(sys.argv[arg])

    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    main()
