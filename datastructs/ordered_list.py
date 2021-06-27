import os
import time

class Node(object):
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class OrderedList(object):
    def __init__(self):
        self.head = None

    def add(self,item):
        #add an item to linked list in the ordered list.
        #search for the position in which the item has to be inserted
        current = self.head
        previous = None
        stop = False
        while current!=None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def remove(self,item):
        #removes the item from linked list
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        
    def search(self,item):
        #searches for an item in the linked list and returns a boolean
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    found = False
                    stop = True
                else:
                    current = current.getNext()
        return found
    
    def size(self):
        #returns the size of the linked list
        current = self.head
        count = 0
        while current != None:
            count+=1
            current = current.getNext()
        return count

    def is_empty(self):
        #checks if the linked list is empty
        size_of_list = self.size()
        return size_of_list == 0

    def index(self,item):
        #returns the position in which the item is present
        current = self.head
        pos = 0
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                print(current.getData())
                found = True
                stop = False
            else:
                if current.getData() > item:
                    stop = True
                else:
                    pos+=1
                    current = current.getNext()
        if found:
            return pos
        else:
            return None
    
    def pop(self,pos):
        #removes and returns the item and given position
        pass

    def pop(self):
        #removes and returns the last item in the list
        pass


if __name__ == '__main__':
    ord_list = OrderedList()
    num_list = [5,10,15,20,25,30]
    for i in num_list:
        ord_list.add(i)
    print("Size of list:", ord_list.size())
    found = ord_list.search(13)
    print(found)
    idx = ord_list.index(2)
    print("Found at index:", idx)
    ord_list.remove(20)
    print("Size of list:", ord_list.size())