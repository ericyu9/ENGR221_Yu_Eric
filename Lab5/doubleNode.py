"""
Name: Eric Yu
Filename: doubleNode.py
Description: Implementation of double node
Date: October 13, 2024
"""

class DoubleNode():

    def __init__(self, value, next=None, previous=None):
        self.__value = value
        self.__nextNode = next
        self.__previousNode = previous 

    #####
    # Methods
    #####
        
    def isFirst(self) -> bool:
        return self.__previousNode == None          #Returns True(first) if there is no previous node
        
    def isLast(self) -> bool:
        return self.__nextNode == None              #Returns True(last) if there is no next node

    #####
    # Getters
    #####

    def getValue(self):
        return self.__value                         #Returns value of the current node
    
    def getNextNode(self):
        return self.__nextNode                      #Returns value of next node

    def getPreviousNode(self):
        return self.__previousNode                  #Returns value of previous node

    #####
    # Setters
    #####

    def setValue(self, new_value) -> None:
        self.__value = new_value                    #Overwrites value for the current node

    def setNextNode(self, new_next) -> None:
        if self.__checkValidNode(new_next):
            self.__nextNode = new_next              #Sets the next node 

    

    def setPreviousNode(self, new_previous) -> None:
        if self.__checkValidNode(new_previous):
            self.__previousNode = new_previous      #Sets the previous node

    #####
    # Helpers
    #####

    def __checkValidNode(self, node) -> bool:       #Checks if the node is a DoubleNode or None
        if type(node) != DoubleNode and node != None:
            raise Exception("Input must be a DoubleNode or None")  #Gives an error if value valid
        
        return True
    
    def __str__(self) -> str:
        return str(self.getValue())                 #Prints the output of the node

if __name__ == "__main__":
    pass