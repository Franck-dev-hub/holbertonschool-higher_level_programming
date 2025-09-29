#!/usr/bin/python3

"""
0-read_file.py
Read a txt file
"""


def read_file(filename=""):
    """
    read_file - Read a txt file
    @filename: Name of the file
    Return: Void
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
