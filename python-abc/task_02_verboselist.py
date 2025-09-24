#!/usr/bin/python3

"""
task_02_verboselist.py
Extend built-in functions
"""


class VerboseList(list):
    """
    VerboseList - Extend built-in classes
    @list: List to extend
    """
    def append(self, item):
        """
        append - Append function
        @item: Item to add
        Return: Void
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        """
        extend - Extend function
        @item: Item to extend the list with
        Return: Void
        """
        super().extend(item)
        print("Extended the list with [{}] item.".format(item))

    def remove(self, item):
        """
        remove - Remove function
        @item: Item to remove
        Return: Void
        """
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        """
        pop - Pop function
        @index: Index to be popped
        Return: Index
        """
        index = super().pop(index)
        priunt("Popped [{}] from the list.".format(index))
        return index
