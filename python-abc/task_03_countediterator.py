#!/usr/bin/python3

"""
task_03_countediterator.py
Extend built-in iterator
"""


class CountedIterator():
    """
    CountedIterator - Counted iterator class
    """
    def __init__(self, data):
        """
        __init__ - Init function
        @data: Data to process
        Return: Void
        """
        self.iterator = iter(data)
        self.counter = 0

    def __next__(self):
        """
        __next__ - Next function
        Return: Next element
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """
        get_count - Get count function
        Return: Counter
        """
        return self.counter
