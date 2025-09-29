#!/usr/bin/python3

"""
11-student.py
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

    def reload_from_json(self, json):
        """
        reload_from_json - Replace all attributes of the Student
        @json: Dict to replace by
        Return: Void
        """
        if "first_name" in json:
            self.first_name = json["first_name"]
        if "last_name" in json:
            self.last_name = json["last_name"]
        if "age" in json:
            self.age = json["age"]
