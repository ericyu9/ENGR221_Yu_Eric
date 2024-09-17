"""
Author: Eric Yu
Filename: myarray.py
Description: Implementation of an unsorted array with duplicates
Date: September 16, 2024
"""

class MyArray():
    # Constructor
    def __init__(self, initialSizeOrValues):
        if type(initialSizeOrValues) is int:
            
            self.__a = [None] * initialSizeOrValues # The array stored as a list of none values
            self.__length = 0                       # Start with no values in the list so the size of the list is zero
            self.__size = initialSizeOrValues       #A new attribute to get the size of array for the append function

        elif type(initialSizeOrValues) is list:
            self.__a = initialSizeOrValues      # The array is stored as a list
            self.__length = len(self.__a)       # The length of the array
            self.__size = len(self.__a)         #Takes the size of a list with elements for append function


    ########
    # Methods
    ########
        
    # Return the current length of the array
    def length(self):
        return self.__length 
    
    # Return a list of the current array values
    def values(self):
        return self.__a

    # Return the value at index idx
    # Otherwise, do not return anything
    def get(self, idx):
      if 0 <= idx and idx < self.__length: # Check if idx is in bounds, and
         return self.__a[idx]              # only return item if in bounds
 
    # Set the value at index idx
    def set(self, idx, value):         
      if 0 <= idx and idx < self.__length:  # Check if idx is in bounds, and
         self.__a[idx] = value              # only set item if in bounds
    
    # Insert value to the end of the array
    def insert(self, value):
        
            if self.__size == 0:            #Checks the size of the array, in this case it is empty.
                self.__a.append(0)          #Adds an element space to the array enabling insert 
                self.__a[0] = value         #The added index is at 0 and is replaced by "Hello"
                self.__length += 1          #Increment the length

            if self.__size >= 1:            #Checks to see if the list contains more than one elements
                self.__a.append(value)      #Adds on "!" at the end of the list
                self.__length += 1          #Increment the length
            

            


    # Return the index of value in the array, 
    # or -1 if value is not in the array
    def search(self, value):

        # Only search the indices we've inserted
        for idx in self.__a: 

            # Check the value at the current index 
            if idx == value:  

                # Return the index  
                return idx  
            
        # Return -1 if value was not found             
        return -1                        

    # Delete the first occurrence of value in the array
    # Returns True if value was deleted, False otherwise
    def delete(self, value):
        
    # Find the index of the value to delete
        idx = self.search(value)
        
        # If the value was found
        while idx != -1:                              #Loops the code when idx has found a value to delete
            
            
            for i in range(self.__length):            #Loops through each index of the list
                if self.__a[i] == value:              #Checks if the value in the index matches the desired element
                    del self.__a[i]                   #Removes the desired element
                    self.__length -= 1                #Reduces size of the list
                    return True
                
            return False
    
    # Print all items in the list
    def traverse(self):
        for i in range(self.__length):
            print(self.__a[i])



if __name__ == '__main__':
    pass
