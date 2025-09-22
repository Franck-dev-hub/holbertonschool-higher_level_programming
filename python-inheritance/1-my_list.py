#!/usr/bin/python3

"""
1-my_list.py
Set inherance
Return a subclass
"""


class MyList(list):
    """
    MyList - Define list methods
    @list - Inherits from list
    Return a subclass
    """
    def print_sorted(self):
        sorted = self.copy()
        sorted.sort()
        print(sorted)
