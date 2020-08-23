"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        # Check for no node in list
        if self.head is None:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1

        else:
            new_node = ListNode(value)
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.head is None:
            return None
        if self.head.next is None:
            head_val = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return head_val
        else:
            head_val = self.head.value
            self.head = self.head.next
            self.length -= 1
            return head_val

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        if self.tail is None:
            new_node = ListNode(value)
            self.tail = new_node
            self.head = new_node
            self.length += 1
        else:
            new_node = ListNode(value)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = None
            self.length += 1
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.tail is None:
            return None
        if self.tail.prev is None:
            tail_val = self.tail.value
            self.tail = None
            self.head = None
            self.length -= 1
            return tail_val
        else:
            tail_val = self.tail.value
            self.tail = self.tail.prev
            self.length -= 1
            return tail_val
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        pass

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    # def delete(self, node):
    #     if node is None:
    #         return None
    #     if node.value is self.head.value:
    #         # val = self.head.value

    #         # self.length -= 1
    #         # return val
    #     if node.value is self.tail.value:
    #         # val = self.tail.value

    #         # self.length -= 1
    #         # return val
    #     else:
    #         val = node.value
    #         node.prev.next = node.next
    #         node.next.prev = node.prev
    #         node.next = None
    #         node.prev = None
    #         self.length -= 1
    #         return val

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current_node = self.head
        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        return max_value

# ! This one stalls tests
    # def get_max(self):
    #     if not self.head:
    #         return None
    #     current_max = self.head.value
    #     current_node = self.head
    #     while current_node:
    #         if current_node.value > current_max:
    #             current_max = current_node.value
    #! Had this further in and stalled tests?
        #         current_node = current_node.next
        # return current_max
