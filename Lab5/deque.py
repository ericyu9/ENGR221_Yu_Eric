"""
Name: Eric Yu
Filename: deque.py
Description: Double ended queue program for a doubly linked list.
Date: October 13, 2024
"""

from .doublyLinkedList import DoublyLinkedList

class Deque():
    def __init__(self):
        self.__values = DoublyLinkedList()              #Initialize Deque with DoublyLinkedList

    def isEmpty(self):
        return self.__values.isEmpty()                  #Checks if Deque is empty     
    
    def __len__(self):
        return len(self.__values)                       #Returns the length of Deque 
    
    def __str__(self):
        return str(self.__values)                       #Returns the printed output of Deque

    def peekLeft(self):
        if self.isEmpty():
            raise Exception("Deque is empty")           #Gives error if Deque is empty
        return self.__values.getFirstNode().getValue()  #Returns the value of the first node

    def peekRight(self):                                
        if self.isEmpty():
            raise Exception("Deque is empty")
        return self.__values.getLastNode().getValue()   #Returns the value of the last node

    def insertLeft(self, value):
        self.__values.insertFront(value)                #Adds a value at the front of Deque
        
    def insertRight(self, value): 
        self.__values.insertBack(value)                 #Adds a value at the end of Deque

    def removeLeft(self): 
        if self.isEmpty():
            raise Exception("Deque is empty")
        
        return self.__values.deleteFirstNode()          #Deletes and returns the value of the first node

    def removeRight(self):
        if self.isEmpty():
            raise Exception("Deque is empty")
        
        return self.__values.deleteLastNode()           #Deletes and returns the  value of the last node
    
if __name__ == "__main__":
    pass