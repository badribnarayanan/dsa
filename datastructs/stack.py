#implementing a stack and it's operations
import os
import time


class Stack(object):
    """Class to create a stack and functions for it's associated operations..
    """
    def __init__(self):
        self.items = []
        self.head = None

    def push(self, item):
        #adds an item to the stack
        self.items.append(item)

    def pop(self):
        #removes the top item from the stack and returns it
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Empty stack. cannot pop items")
            return None

    def size(self):
        #returns the size of the stack
        return len(self.items)

    def peek(self):
        #returns the top item in the stack without removing the item
        return self.items[len(self.items)-1]

    def is_empty(self):
        #checks if the stack is empty or not and returns the boolean value
        return self.items == [] 


if __name__ == '__main__':
    stack = Stack()
    stack.push('fat fuck')
    stack.push('maami')
    stack.push(4)
    print("Size of stack:", stack.size())
    print("Last item in stack:", stack.peek())

        