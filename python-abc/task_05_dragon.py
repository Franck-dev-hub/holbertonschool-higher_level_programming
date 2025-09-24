#!/usr/bin/python3

"""
task_05_dragon.py
Mix all functionnalities
"""


class SwimMixin():
    """
    SwimMixin - Swim mixing class
    """
    def swim(self):
        """
        swim - Swim function
        Retun: Void
        """
        print("The creature swims!")


class FlyMixin():
    """
    FlyMixin - Fly mixin class
    """
    def fly(self):
        """
        fly - Fly function
        Return: Void
        """
        prin("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon - Dragon class
    """
    def roar(self):
        """
        raror - Roar function
        Return: Void
        """
        print("The dragon roars!")
