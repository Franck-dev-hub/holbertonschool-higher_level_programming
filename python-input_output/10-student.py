#!/usr/bin/python3

"""
10-student.py
Write a class that define a student
"""


class Student():
    """
    Student - Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        __init__ - Init new student
        @first_name: First name of the student
        @last_name: Last name of the student
        @age: Age of the student
        Return: Void
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to_json - Retrieve dict representation of a Student instance
        @attrs: Attributes list
        Return: Dict representation
        """
        if not isinstance(attrs, list):
            return self.__dict__

        for attribute in attrs:
            if not isinstance(attribute, str):
                return self.__dict__

        dictionary = {}
        for attribute in attrs:
            if attribute in self.__dict__:
                dictionary[attribute] = self.__dict__[attribute]
        return dictionary
