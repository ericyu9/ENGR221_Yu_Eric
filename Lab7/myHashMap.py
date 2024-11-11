"""
Author: Eric Yu
Filename: myHashMap.py
Description: Implements a hash map with methods to add, remove, delete and replace keys.
Date: October 26, 2024
"""

class MyHashMap:
    def __init__(self, load_factor=0.75,
                       initial_capacity=16):
        self.load_factor = load_factor 
        self.capacity = initial_capacity 
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    """
    Resizes the self.buckets array when the load_factor is reached. """
    def resize(self):
        # Double the number of buckets
        self.capacity *= 2 
        # Create a new set of buckets that's twice as big as the old one
        new_buckets = [[] for _ in range(self.capacity)]
        # Add each key, value pair already in the MyHashMap to the new buckets
        for bucket in self.buckets:
            if bucket != []:
                for entry in bucket:
                    self.put(entry.getKey(), entry.getValue())
        # Update the self.buckets attribute with the new entries
        self.buckets = new_buckets


    def put(self, key, value):
        keyHash = hash(key)                                         #Generates a hash to store the key value pair   

        if key == None:
            raise Exception("Key cannot be None")                   #Raise an exception if key is None
        
        if ((self.size + 1)/self.capacity) > self.load_factor:      #Resize hash map when adding new when it would surpass load factor
            self.resize()

        bucket = self.buckets[keyHash]                              #Access bucket with the hash value

        for entry in bucket:
            if entry.getKey() == key:                               #Checks for existing key
        
                return False

        bucket.append(self.MyHashMapEntry(key, value))              #Appends the key value pair
        self.size += 1                                              #Increase hash map size by 1
        
        return True

        

    def replace(self, key, newValue):
        if key == None:
            raise Exception("Key cannot be None")
        
        keyHash = hash(key)
        bucket = self.buckets[keyHash]

        for entry in bucket:                                    
            if entry.getKey() == key:                           #Searches for specified key 
                entry.setValue(newValue)                        #Updates the value of specified key 

                return True
        
        return False


    def remove(self, key):
        if key == None:
            raise Exception("Key cannot be None")
        
        keyHash = hash(key)
        bucket = self.buckets[keyHash]

        for i in range(len(bucket)):                            #Iterates through and access the index of buckets
            entry = bucket[i]                                   

            if entry.getKey() == key:                       
                del bucket[i]                                   #Remove the entry in the bucket index
                self.size -= 1                                  #Reduces the size of hash map   

                return True
        
        return False


    def set(self, key, value):
        if key == None:
            raise Exception("Key cannot be None")

        keyHash = hash(key) 
        bucket = self.buckets[keyHash]

        if ((self.size + 1)/self.capacity) > self.load_factor:
            self.resize()

        for entry in bucket:                    
            if entry.getKey() == key:                               #Checks if specified key exists in the hash map
                entry.setValue(value)                               

                return True                                     
            
        bucket.append(self.MyHashMapEntry(key, value))              #Appends a new key value pair if the loop doesn't return True(key existed)
        self.size += 1                                              #Increase hash map size


    def get(self, key):
        if key == None:
            raise Exception("Key cannot be None")
        
        keyHash = hash(key)
        bucket = self.buckets[keyHash]

        for entry in bucket:
            if entry.getKey() == key:
                return entry.getValue()
        
        return None
        

    def size(self):
        return self.size                        #Returns size of hash map


    def isEmpty(self):
        return self.size == 0                   #Returns True or False whether hash map contains any keys


    def containsKey(self, key):
        if key == None:
            raise Exception("Key cannot be None")

        keyHash = hash(key) 
        bucket = self.buckets[keyHash]

        for entry in bucket:
            if entry.getKey() == key:
                return True                     #Returns True when specified key is found
        
        return False


    def keys(self):
        keys = []                               #Initialize the list
        
        for bucket in self.buckets:
            for entry in bucket:
                keys.append(entry.getKey())     #Puts together a list filled with keys if there is any
                
        
        return keys                             #Returns the list

    class MyHashMapEntry:
        def __init__(self, key, value):
            self.key = key 
            self.value = value 

        def getKey(self):
            return self.key 
        
        def getValue(self):
            return self.value 
        
        def setValue(self, new_value):
            self.value = new_value 


if __name__ == "__main__":
    map = MyHashMap()
    print("isEmpty:", map.isEmpty())
    print("Putting (1, 'rat'):", map.put(1, "rat"))
    print("Replacing (1, 'mouse'):", map.replace(1, "mouse"))
    print("Removing (1, 'mouse)", map.remove(1))
    print("Setting (1, 'cat')", map.set(1, "cat"))
    print("Getting (1, 'cat')", map.get(1))
    print("Size:", map.size)
    print("Putting (2, 'dog')", map.put(2, "dog"))
    print("Contains (1)", map.containsKey(1))
    print("List:", map.keys())
    print("isEmpty:", map.isEmpty())