#!/usr/bin/python3

"""
task_04_flyingfish.py
Multiple class inherance
"""


class Fish():
    """
    Fish - Fish class
    """
    def swim(self):
        """
        swim - Swim function
        Return: Void
        """
        print("The fish is swimming")

    def habitat(self):
        """
        habitat - Habitat function
        Return: Void
        """
        print("The fish lives in water")


class Bird():
    """
    Bird - Bird class
    """
    def fly(self):
        """
        fly - Fly function
        Return: Void
        """
        print("The bird is flying")

    def habitat(self):
        """
        habitat - habitat function
        Return: Void
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish - Flying fish class
    @Fish: Fish class
    @Bird: Bird class
    """
    def fly(self):
        """
        fly - Fly function
        Return: Void
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        swim - Swim function
        Return: Void
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        habitat - Habitat function
        Return: Void
        """
        print("The flying fish lives in water and the sky!")
