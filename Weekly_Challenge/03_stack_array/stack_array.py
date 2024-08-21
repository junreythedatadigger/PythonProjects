# Implement a stack using an array. A stack follows the Last In,
# First Out (LIFO) principle. Implement the following operations:
#
# push(element) - Adds an element to the top.
# pop() - Removes and returns the top element.
# peek() - Returns the top element without removing it.
# isEmpty() - Checks if the stack is empty.

class Stack:

    def __init__(self, stack_array=[]):
        self.stack_array = stack_array

    def push(self, element):
        self.stack_array.append(element)
        return self.stack_array

    def pop(self):
        last_element = self.stack_array[-1]
        self.stack_array.pop(-1)
        return last_element

    def peek(self):
        last_element = self.stack_array[-1]
        return last_element

    def is_empty(self):
        if len(self.stack_array) == 0:
            return True
        else:
            return False
