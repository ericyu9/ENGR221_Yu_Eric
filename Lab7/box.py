from myHashMap import MyHashMap
from entry import Entry

class Box:
    def __init__(self):
        self.nicknameMap = MyHashMap()
        self.populateBox()

    """
    Adds Entries to the Box from inputFile. Assume that each
    line in inputFile corresponds to an Entry."""
    def populateBox(self, inputFile = 'C:/Users/vaine/OneDrive/Documents/ENGR221_Yu_Eric/Lab7/entries.txt'):
        #Open the file as read only
        with open(inputFile, 'r') as f:
            #Add each value in the file as an Entry to the box
            for line in f:
                # Set the first word in the line as the nickname, and 
                # the second as species
                nickname, species = line.split()
                # Add the new entry to the Box
                self.add(nickname, species)
        

    def add(self, nickname, species):

        if self.nicknameMap.containsKey(nickname):              #Checks if nickname already exists in box
            
            return False

        entry = Entry(nickname, species)                        #Creates new entry
        self.nicknameMap.put(nickname, entry)                   #Adds entry to box

        return True


    def find(self, nickname, species):                          

        entry = self.nickname.get(nickname)                     #Creates entry with associated nickname 

        if entry != None & entry.getSpecies() == species:       #Checks if entry is an actual nickname and matches the species 

            return entry
        
        return None



    def findAllNicknames(self):

        names = self.nicknameMap.keys()                         #Makes names a list of keys

        if names:                                               #If names list contains names it will return a list of nicknames

            return names
        
        else:

            return []                                           #Return empty list

 
    def findEntryByNickname(self, nickname):

        if self.nicknameMap.containsKey(nickname):

            return self.nicknameMap.get(nickname)               #Returns entry with given nickname
        
        else:

            return []


    def removeByNickname(self, nickname):

        if self.nicknameMap.containsKey(nickname):

            self.nicknameMap.remove(nickname)                   #Removes the entry of specified nickname
            return True
        
        return False


    def removeEntry(self, nickname, species):
        
        if self.nicknameMap.containsKey(nickname):              
            entry = self.nicknameMap.get(nickname)              #Checks nickname entry

            if entry.getValue() == species:                     #Checks if specified nickname of entry matches the species associated to it

                self.nicknameMap.remove(nickname)               
                return True
        
        return False

if __name__ == '__main__':
    box = Box()
    print("Adding Meowy, cat", box.add("Meowy", "cat"))
    