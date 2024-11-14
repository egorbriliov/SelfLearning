# Create a Node class to create a node
from enum import Enum


class Position(Enum):
    START: str = "start"
    END: str = "END"
    INDEX: int


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def insert(self, data, position: Position | int = Position.END):
        """
        Method to add a node at any index
        Indexing starts from 0.
        """
        if self.head is not None:
            while self.head.next is not None:
                self.head = self.head.next
            else:
                self.head.next = Node(data)
        else:
            self.head = Node(data)



    def remove_first_node(self):
        """
        Method to remove first node of linked list
        """
        if self.head is None:
            return

        self.head = self.head.next

    def update_node(self, val, index):
        """
        Update node of a linked list
        at given position
        """
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while current_node is not None and position != index:
                position = position + 1
                current_node = current_node.next

            if current_node is not None:
                current_node.data = val
            else:
                print("Index not present")

    def remove_last_node(self):
        """Method to remove last node of linked list"""
        if self.head is None: return
        current_node = self.head
        while current_node is not None and current_node.next.next is not None:
            current_node = current_node.next

        current_node.next = None

    def remove_at_index(self, index):
        """Method to remove at given index"""
        if self.head is None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while current_node is not None and position + 1 != index:
                position = position + 1
                current_node = current_node.next

            if current_node is not None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    def remove_node(self, data):
        """ Method to remove a node from linked list"""

        current_node = self.head

        if current_node.data == data:
            self.remove_first_node()
            return

        while current_node is not None and current_node.next.data != data:
            current_node = current_node.next

        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next

    @property
    def size(self) -> int:
        """
        Print the size of linked list
        """
        size = 0
        if self.head:
            current_node = self.head
            while current_node:
                size = size + 1
                current_node = current_node.next
            return size
        else:
            return 0

    def all(self) -> list:
        required: list = []
        while self.head.next is not None:
            required.append(self.head.data)
            self.head = self.head.next
        return required

# create a new linked list

llist = LinkedList()

llist.insert("zxc")
llist.insert(3123)

print(llist.all())