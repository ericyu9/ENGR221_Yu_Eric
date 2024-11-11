"""
Author: Eric Yu
Filename: doublyLinkedList.py
Description: Implementation of a doubly linked list using double nodes
Date: October 13, 2024
"""

from .doubleNode import DoubleNode 

class DoublyLinkedList:

    def __init__(self):
        self.__firstNode = None
        self.__lastNode = None 

    def isEmpty(self):
        return self.getFirstNode() == None                              #Checks if list is empty

    def first(self):                                                    
        if self.isEmpty():
            raise Exception("List is empty")                            #Gives an error if List is empty
        return self.getFirstNode().getValue()                           #Returns the value of the first node
    
    def getFirstNode(self):
        return self.__firstNode                                         #Returns value of the first node

    def getLastNode(self):
        return self.__lastNode                                          #Returns value of the last node
    
    def setFirstNode(self, node):
        if node != None and type(node) != DoubleNode:                   
            raise Exception("Input must be a valid Node or None")       #Checks if value is valid
        
        self.__firstNode = node                                         #Replaces first node with current node

    def setLastNode(self, node):
        if node != None and type(node) != DoubleNode:
            raise Exception("Input must be a valid Node or None")
        
        self.__lastNode = node                                          #Replaces last node with current node

    def find(self, value) -> DoubleNode:                                #Searches Nodes for value
        node = self.getFirstNode()                                      
        
        while node != None:
            if node.getValue() == value:
                return node                                             #Return value if found
            
            node = node.getNextNode()                                   #Iterates next node
        
        return None  

    def insertFront(self, value):
        new_node = DoubleNode(value, self.getFirstNode())               #Insert a new node of the value at the front of list
        
        if self.isEmpty():
            self.setLastNode(new_node)                                  #Updates the node if list was empty
        
        else:
            self.getFirstNode().setPreviousNode(new_node)               #Moves the old first node to a new node
        
        self.setFirstNode(new_node)                                     #Update the first node

    def insertBack(self, value):
        new_node = DoubleNode(value, None, self.getLastNode())          #Insert a new node of the value at the back of the list
        
        if self.isEmpty():
            self.setFirstNode(new_node)                                 #Updates the node if list was empty
        
        else:
            self.getLastNode().setNextNode(new_node)                    #Moves the old last node to a new node
        
        self.setLastNode(new_node)                                      #Update the last node

    def insertAfter(self, value_to_add, after_value):
        node = self.find(after_value)                                   #Finds the node to insert after
        
        if node == None:
            return False
        
        new_node = DoubleNode(value_to_add, node.getNextNode(), node)   
        
        if node.getNextNode() != None:
            node.getNextNode().setPreviousNode(new_node)                #Moves the next node to a new node
        
        node.setNextNode(new_node)                                      #Updates current node to new node
        
        if new_node.getNextNode() == None:                  
            self.setLastNode(new_node)                                  #Updates last node with new node
        
        return True

    def deleteFirstNode(self):                                          
        if self.isEmpty():
            raise Exception("List is empty")                            #Gives error if list is empty
        
        first = self.getFirstNode()
        self.setFirstNode(first.getNextNode())                          #Update first node to next node
        
        if self.getFirstNode() != None:
            self.getFirstNode().setPreviousNode(None)                   #Updates node to None
        
        else:
            self.setLastNode(None)                                      #Updates the last node to None
       
        return first.getValue()                                         #Returns the value of the deleted node
    
    def deleteLastNode(self):
        if self.isEmpty():
            raise Exception("List is empty")
        
        last = self.getLastNode()
        self.setLastNode(last.getPreviousNode())                        #Update last node to previous node
        
        if self.getLastNode() != None:
            self.getLastNode().setNextNode(None)                        #Updates last node to None
        
        else:
            self.setFirstNode(None)                                     #Updates first node to None
        
        return last.getValue()                                          #Returns the value of deleted node
    
    def deleteValue(self, value):
        if self.isEmpty():
            raise Exception("List is empty; cannot delete")
       
        current = self.getFirstNode()
        
        while current != None:
            if current.getValue() == value:    
                if current.getPreviousNode() != None:
                    current.getPreviousNode().setNextNode(current.getNextNode())
                
                else:
                    self.setFirstNode(current.getNextNode())            #Updates first node if it is to be deleted
                
                if current.getNextNode() != None:
                    current.getNextNode().setPreviousNode(current.getPreviousNode())
                
                else:
                    self.setLastNode(current.getPreviousNode())         #Updates last node if it is to be deleted
                
                return current.getValue()                               #Returns the value of deleted node
            
            current = current.getNextNode()
        raise Exception("Value not found")                              #Raise an exception if no value is found

    def forwardTraverse(self):
        node = self.getFirstNode()                      
        
        while node != None:
            print(node.getValue())                                      #Prints the value of current node
            node = node.getNextNode()                                   #Traverse list from front to back

    def reverseTraverse(self):
        node = self.getLastNode()
        
        while node != None:
            print(node.getValue())
            node = node.getPreviousNode()                               #Traverse list from back to front

    def __len__(self):
        length = 0
        node = self.getFirstNode()
        
        while node != None:
            length += 1
            node = node.getNextNode()
        
        return length                                                   #Returns length of list
    
    def __str__(self):
        out = "["
        node = self.getFirstNode()
        
        while node != None:
            if len(out) > 1:
                out += " <-> "
            
            out += str(node)
            node = node.getNextNode() 
        
        return out + "]"                                                #Returns printed output of list
    
if __name__ == "__main__":
    pass
