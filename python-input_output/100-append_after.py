#!/usr/bin/python3

"""
100-append_after.py
Insert a text after a specific text
"""

def append_after(filename="", search_string="", new_string=""):
    """
    append_after - Append a text after an other
    @filename: Name of the output file
    @search_string: String to search
    @new_string: String to add
    Return: Void
    """
    with open(filename, 'r', encoding="utf-8") as file:
        content = file.readlines()

    new_lines = []
    for line in content:
        new_lines.append(line) 
        if search_string in line:
            new_lines.append(new_string)

    with open(filename, 'w', encoding="utf-8") as file:
        file.writelines(new_lines)
