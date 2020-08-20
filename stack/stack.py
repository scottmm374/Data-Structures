"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""

# Array Stack


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.insert(0, value)

#     def pop(self):
#         if len(self.storage) >= 1:
#             val = self.storage[0]
#             self.storage.pop(0)
#             return val
#         else:
#             return None


# Stack class for Linked List

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size = self.size + 1
        return value

    def pop(self):
        if self.size >= 1:
            val = self.storage.remove_head()
            self.size = self.size - 1
            return val
        else:
            return None


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        # stores a node that is beginning of list
        self.head = None
        # stores a node that is the end of the list
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:  # list is empty
            self.head = new_node
            self.tail = new_node

        else:
            # point current tail to the new_node
            self.tail.next_node = new_node
            # Then move tail to new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:   # list is empty, so nothing to do
            return None
        # Checking here if only one element in the list (If next node is none, then we know 1 element in list)
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        else:
            # If we have more elements in the list
            head_value = self.head.value    # Grabbing the current head value I think
        # Then pointing the next.node to head, which removed pointer from current head
            self.head = self.head.next_node
            return head_value

    def remove_tail(self):
        if not self.tail:
            return None
        current_node = self.head
        # there is only on elemenet in the list, so remove it.
        if current_node.next_node is None:
            tail_value = self.tail.value
            self.head = None
            self.tail = None
            return tail_value
        else:
            if current_node.next_node is self.tail:
                tail_value = current_node.next_node.value
                self.tail = current_node
                current_node.next_node = None
                return tail_value
