"""
Author: Eric Yu
Filename: SearchStructures.py
Description: Stack and queue data structures with methods to check if it is empty and adds or remove items.
Date: September 29, 2024
"""

# Implementation of a Stack
class Stack():
    def __init__(self):
        self.__items = []

    # Returns True if the Stack is empty, or False if it is not empty
    def isEmpty(self):
        if len(self.__items) == 0:          #Checks if list is empty based on list length
            return True
        else:
            return False

    # For a Stack, this should "push" item to the top of the Stack
    def add(self, item):
        self.__items.append(item)           #Adds an item to the end(top) of the list

    # For a Stack, this should "pop" an item from the Stack
    # and return it
    def remove(self):
        if not self.isEmpty():              #Checks if list is empty
            return self.__items.pop()       #Removes the item from end(top) of the list
        
    
# Implementation of a Queue
class Queue():
    def __init__(self):
        self.__items = []

    # Returns True if the Queue is empty, or False if it is not empty
    def isEmpty(self):
        if len(self.__items) == 0:          #Checks if list is empty based on list length
            return True
        else:
            return False

    # For a Queue, this should "enqueue" item to the end of the Queue
    def add(self, item):
        self.__items.append(item)               #Adds an item to the end(top) of the list

    # For a Queue, this should "dequeue" an item from the Queue
    # and return it
    def remove(self):
        if not self.isEmpty():
            return self.__items.pop(0)          #Removes item from the front(bottom) of the list
    
    