#!/usr/bin/python3

"""
task_00_abc.py
Define an abstract method
Return a string
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Animal - Main abstract animal class
    @ABC: Abstract module
    """
    @abstractmethod
    def sound(self):
        """
        sound - Main abstract function
        Return: Void
        """
        pass


class Dog(Animal):
    """
    Dog - Main dog class
    @Animal: Parent class
    """
    def sound(self):
        """
        sound - Dog's sound function
        Return: String
        """
        return "Bark"


class Cat(Animal):
    def sound(self):
        """
        sound - Cat's sound function
        Return: String
        """
        return "Meow"
