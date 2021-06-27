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


class UnorderedList(object):
    def __init__(self):
        self.head = None

    def add(self,item):
        #add an item to linked list
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

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
        while current != None and not found:
            if current.getData() == item:
                found = True
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
        max = self.size()-1
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                max-=1
                current = current.getNext()
        if found:
            return max
        else:
            return None
    
    def insert(self,pos,item):
        #inserts given item at position pos
        pass

    def append(self,item):
        #appends item to end of list
        pass

    def pop(self,pos):
        #removes and returns the item and given position
        pass

    def pop(self):
        #removes and returns the last item in the list
        pass


if __name__ == '__main__':
    unord_list = UnorderedList()
    num_list = [15,30,5,20,25,10]
    for i in num_list:
        unord_list.add(i)
    print("Size of list:", unord_list.size())
    found = unord_list.search(13)
    print(found)
    idx = unord_list.index(25)
    print("Found at index:", idx)
    unord_list.remove(20)
    print("Size of list:", unord_list.size())


        
