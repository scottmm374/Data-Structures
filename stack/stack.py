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

    def __str__(self):
        return f'{self.size} : {self.storage}'

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_head()


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        output = " "
        current = self.head
        while current is not None:
            output += f'{current.value} ->'
            current = current.next_node

        return output

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def add_to_head(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def remove_head(self):
        if not self.head:
            print("wrong spot")
            return None
        elif self.head.next_node is None:
            head = self.head
            self.head = None
            self.tail = None
            print(head.value, "if one node")
            return head.value
        else:
            head = self.head
            self.head = self.head.next_node
            print(head.value, "more then one")
            return head.value

    def remove_tail(self):
        if not self.tail:
            return None
        current_node = self.head
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


testing_list = Stack()
print(testing_list, "1")
testing_list.push(100)
print(testing_list.size, "length")
print(testing_list, "2")
testing_list.push(101)
print(testing_list.size, "length")
print(testing_list, "3")
testing_list.push(105)
print(testing_list.size, "length")
print(testing_list, "4")
testing_list.pop()
print(testing_list.size, "length")
print(testing_list, "pop 1")
testing_list.pop()
print(testing_list.size, "length")
print(testing_list, "pop 2")
testing_list.pop()
print(testing_list.size, "length")
print(testing_list, "pop 3")
print(testing_list, "list")
