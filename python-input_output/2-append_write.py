#!/usr/bin/python3

"""
2-append_write.py
Write in a file
"""


def append_write(filename="", text=""):
    """
    append_write - Append text to a file
    @filename: Name of the file
    @text: Text to add
    Return: Number of char written
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
