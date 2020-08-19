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
            # !(Not sure exactly why we return the head_value?)
            return head_value

        # If we have more elements in the list
        head_value = self.head.value    # Grabbing the current head value I think
        # Then pointing the next.node to head, which removed pointer from current head
        self.head = self.head.next_node
        return head_value

    def remove_tail(self):
        if not self.tail:
            return None

        # there is only on elemenet in the list, so remove it.
        if self.head.next_node is None:
            tail_value = self.tail.value
            self.head = None
            self.tail = None
            return tail_value
        else:
            current_node = self.head.value
            if current_node.next_node is None:
                tail_value = self.tail.value
                self.tail = current_node
                current_node.next_node = None
                return tail_value
