#implementing a queue and it's operations
import os
import time


class Queue(object):
    def __init__(self):
        self.items = []
        self.head = None

    def enqueue(self, item):
        #adds an item to the queue
        self.items.insert(0,item)

    def dequeue(self):
        #removes the top item from the queue and returns it
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Empty queue. cannot pop items")
            return None

    def size(self):
        #returns the size of the queue
        return len(self.items)

    def is_empty(self):
        #checks if the queue is empty or not and returns the boolean value
        return len(self.items) == []


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('fat fuck')
    queue.enqueue('maami')
    queue.enqueue(4)
    print("Size of queue:", queue.size())
    print(queue.items)
    queue.dequeue()
    print("Size of queue after dequeue:", queue.size())
    print(queue.items)

        