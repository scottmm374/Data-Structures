"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
# from stack import Stack


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    # def __str__(self):
    #     return f'{self.size} : {self.storage}'

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.pop()


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree

    def insert(self, value):
        # compare values to detrmine direction
        if value >= self.value:
            # if there is no node on the right, insert value
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # Same as
                # right_child = self.right
                # right_child = BSTNode(value)
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

                # Return True if the tree contains the value
                # False if it does not

    # def contains(self, target):
    #     # Contains:
    #     # Compare target value to node.value
    #     if target == self.value:
    #         return True
    #         # ! CHECKING RIGHT
    #     if target > self.value:
    #         # If no NODE were DONE
    #         if self.right == None:
    #             return False
    #             # If NODE check target against Right Value
    #         elif self.right.value == target:
    #             return True
    #         else:
    #             # Calling function again on RIGHT side of tree
    #             self.right.contains(target)
    #         # ! CHECKING THE LEFT
    #     else:
    #         # If no NODE were DONE
    #         if self.left == None:
    #             return False
    #             # If NODE check target against Right Value
    #         elif self.left.value == target:
    #             return True
    #         else:
    #             # Calling function again on left side of tree
    #             self.left.contains(target)


#     # Return the maximum value found in the tree

    # def get_max(self):
    #     if self.right is None:
    #         return self.value
    #     else:
    #         max_value = self.right.get_max()
    #         return max_value

    #         #     # Call the function `fn` on the value of each node

    # def for_each(self, fn):

    #     if self.left is not None:
    #         self.left.for_each(fn)

    #     fn(self.value)

    #     if self.right is not None:
    #         self.right.for_each(fn)


# Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self):

        if self.value is None:
            return
        if self.left:
            self.left.in_order_print()

        print(self.value)

        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

        # Print the value of every node, starting with the given node,
        # in an iterative depth first traversal

    # def dft_print(self):
    #     curr_node = self
    #     stack = Stack()
    #     stack.push(curr_node)

    #     while len(stack) > 0:
    #         curr_node = stack.pop()
    #         print(curr_node.value)

    #         if curr_node.left is not None:
    #             stack.push(curr_node.left)

    #         if curr_node.right is not None:
    #             stack.push(curr_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)
# bst = BSTNode(8)


bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.bft_print()
# print("DFT print")
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
print("in order")
bst.in_order_print()
# print("post order")
# bst.post_order_dft()
