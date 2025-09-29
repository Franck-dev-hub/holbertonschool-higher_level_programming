#!/usr/bin/python3

"""
1-write_file.py
Write in a file
"""

def write_file(filename="", text=""):
    """
    write_file - Write in a file
    @filename: Name of the file
    @text: Text to insert
    Return: Number of char written
    """
    counter = 0
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
