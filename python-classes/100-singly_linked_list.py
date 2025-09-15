#!/usr/bin/python3

"""
100-singly_linked_list.py
This module define a singly linked list
Return: Void
"""

class Node:
    """
    Define a node
    """
    def __init__(self, data: int, next_node: "Node" = None):
        """
        __init__ - Init a new node
        @data: Node's data
        @next_node: Next node
        Return: Void
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """
        data - Get node data
        Return: int - Data
        """
        return self.__data

    @data.setter
    def data(self, value: int):
        """
        data - Set node data
        @value: Value of the node
        Return: Value of the node
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        next_node - Get the next node
        Return: Node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value: "Node"):
        """
        next_node - Set the next node
        @value: Value of the node
        Return: Value of the node
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """
    Define a singly linked list
    """
    def __init__(self):
        """
        __init__ - Init a new singly linked list
        Return: Void
        """
        self.__head = None

    def __str__(self):
        """
        __str__ - Convert to str
        Return: str - Node content
        """
        result = ""
        current = self.__head
        while current:
            result += str(current.data)
            if current.next_node:
                result += "\n"
            current = current.next_node
        return result

    def sorted_insert(self, value: Node):
        """
        sorted_insert - Insert a new node in increasing order
        @value: Value of the node
        Return: Void
        """
        new_node = Node(value)

        if self.__head is None or self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
