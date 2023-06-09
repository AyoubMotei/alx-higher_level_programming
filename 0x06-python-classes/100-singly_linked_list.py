#!/usr/bin/python3
"""This script defines the Node and SinglyLinkedList classes"""

class Node:
    """
    A class that represents a Node object.

    Attributes:
        data: data field of node.
    """
    def __init__(self, data, next_node=None):
        """Creates a new instance of the Node class.

        Args:
            __data : data field of node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data stored in the node.

        Returns: the data field of a node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node.

        Args:
            value (int): data field of a node.

        Raises:
            TypeError: data must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node linked to the current node.

        Returns: The next_node instance.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node linked to the current node.

        Args:
            value (None): next node of a Node.

        Raises:
            TypeError: next_node must be a Node object .
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class that represents a Singly Linked List.

    Attributes:
        head: head of the SinglyLinkedList.
    """
    def __init__(self):
        """Creates a new instance of the SinglyLinkedList class .

        Args:
            __head : head of the SinglyLinkedList .
        """
        self.__head = None

    def __str__(self):
        """Returns a string representation of the class object.

        Returns: The class object represented as a string.
        """
        temp_var = self.__head
        print_node = []
        while temp_var:
            print_node.sort()
            print_node.append(str(temp_var.data))
            temp_var = temp_var.next_node

        print_node.sort(key=int)
        return ("\n".join(print_node))

    def sorted_insert(self, value):
        """Inserts a new node in sorted order.

        Args:
            value: value.
        """
        if self.__head is None:
            new_node = Node(value)
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            new_node = Node(value)
            new_node.data = value
            new_node.next_node = self.__head
            self.__head = new_node
