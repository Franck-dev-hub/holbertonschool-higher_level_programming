#!/usr/bin/python3

"""
5-text_indentation.py
This module prints a text with 2 new lines after each of these characters: ., ? and :
Return: Void
"""


def text_indentation(text):
    """
    text_indentation - Indent text
    @text: Text to indent
    Return: Void
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    temp = ""
    for char in text:
        temp += char
        if char in ".,?:":
            print(temp.strip(), end="\n\n")
            temp = ""

    if temp.strip() != "":
        print(temp.strip(), end="")
