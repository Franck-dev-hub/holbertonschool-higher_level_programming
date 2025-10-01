#!/usr/bin/python3

"""
task_01_pickle.py
Serialize & deserialize with pickle
"""

import pickle


class CustomObject():
    """
    CustomObject - Custom object
    """
    def __init__(self, name: str, age: int, is_student: bool):
        """
        __init__ - Init function
        @name: Name of the student
        @age: Age of the student
        @is_student: Is student or not
        Return: Void
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """
        serialize - Serialize the current instance
        @filename: Name of the file
        Return: Void
        """
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        deserialize - Deserialize function
        @filename: Name of the file
        Return: The object deserilalized
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                return None
        except (FileNotFoundError, EOFError):
            return None
        else:
            return obj

    def display(self):
        """
        display - Display informations
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))
