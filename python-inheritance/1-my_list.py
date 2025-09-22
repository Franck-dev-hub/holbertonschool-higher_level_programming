#!/usr/bin/python3

"""
1-my_list.py
Set inherance
Return a subclass
"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
