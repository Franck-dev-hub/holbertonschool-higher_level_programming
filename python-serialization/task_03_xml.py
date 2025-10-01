#!/usr/bin/python3

"""
task_03_xml.py
Serialize to xml
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    serialize_to_xml - Serialize data to xml
    @dictionary: Dictionary to serialize
    @filename: Name of the file where dict will be saved
    Return: Void
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    ET.ElementTree(root).write(filename)


def deserialize_from_xml(filename):
    """
    deserialize_from_xml - Deserialize from xml file
    Return: Deserialized dictionary
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
