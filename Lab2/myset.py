class MySet:
    def __init__(self, values=None):            #Initializes the list with values and size
        
        self.__values = []                      #List to hold values of the given list
        self.__size = 0                         #Stores the number of elements in the list

        if values != None:
            for val in values:
                self.insert(val)                #Prevents duplicates using the insert function

    def search(self, value):                    #Search for desired value in the list
        
        for i in self.__values:                 #Loops through the values in the list
            if i == value:
                return True                    
        return False

    def insert(self, value):                    #Inserts desired value into the list and changes size
        
        if not self.search(value):              #Checks if the value is already in the list or not
            self.__values.append(value)         #Adds the desired value
            self.__size += 1                    #Increases the size of the list

    def delete(self, value):                    #Deletes desired value of the list and changes size
        
        for i in range(self.__size):            #Loops through each index of the list
            if self.__values[i] == value:       #Checks if the value in the index matches the desired element
                del self.__values[i]            #Removes the desired element
                self.__size -= 1                #Reduces size of the list
                return True
                
        return False

    def traverse(self):                         #Prints each value in the list
        
        for i in self.__values:
            print(i)
    
    def size(self):                             #Return the number of values in the list for other functions
        
        return self.__size

    def vals(self):                             #Returns the values in the list
        
        return self.__values
