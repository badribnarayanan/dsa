#implementing a queue and it's operations
import os
import time


class CircularQueue(object):
    def __init__(self):
        self.items = []
        self.head = None

    def add_front(self,item):
        #adds an item to the front of the queue
        self.items.insert(0,item)

    def add_rear(self,item):
        #adds an item to the rear of the queue
        self.items.append(item)

    def remove_front(self):
        #removes the front item from the queue and returns it
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Empty queue. cannot pop items")
            return None
    
    def remove_rear(self):
        #removes the front item from the queue and returns it
        if not self.is_empty():
            return self.items.pop(0)
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
    circular_queue = CircularQueue()
    circular_queue.add_front('fat fuck')
    circular_queue.add_front('maami')
    circular_queue.add_rear('bachmann')
    circular_queue.add_rear('slimy fuck')
    print("Size of queue:", circular_queue.size())
    print(circular_queue.items)
    circular_queue.remove_front()
    print("Size of queue after dequeue:", circular_queue.size())
    print(circular_queue.items)
    circular_queue.remove_rear()
    print("Size of queue after dequeue:", circular_queue.size())
    print(circular_queue.items)

        