"""
Author: Eric Yu
Filename: binarySearchTree.py
Description: Implementation of a binary search tree
Date: November 11, 2024
"""

class BinarySearchTree:
    """ DESCRIBE THE BST CLASS HERE
        The implemented BST has insertion, deletion, search, traverse, and succession methods.
        The tree has the properties of the left branch having smaller keys and the right branch having larger keys. 
    """

    def __init__(self):
        self.__root = None # The root Node of this BST

    def insert(self, insertKey, insertValue):
        """ Inserts the given key and value into the BST.
            Inputs:
                - insertKey: (any) The key to insert
                - insertValue: (any) The value to insert
            Returns: None
        """
        # Update the root to include the inserted node
        self.__root = self.__insertHelp(self.__root, insertKey, insertValue)
    
    def __insertHelp(self, node, insertKey, insertValue):
        """ A recursive helper method to insert a new node 
            with the given key and value into the BST.
            Inputs:
                - node: (Node) The root of the subtree to insert into
                - insertKey: (any) The key to insert
                - insertvalue: (any) The value to insert
            Returns: The node to insert """
        # Base case - Insert the node as a leaf in the appropriate location
        if node == None:
            return self.__Node(insertKey, insertValue)
        # Insert the key into the left subtree if it is less than the current key
        elif insertKey < node.key:
            node.left = self.__insertHelp(node.left, insertKey, insertValue)
        # Insert the key into the right subtree if it is greater than the current key
        elif insertKey > node.key:
            node.right = self.__insertHelp(node.right, insertKey, insertValue)
        # Return the node with the node inserted
        return node

    def isEmpty(self):
        """ ISEMPTY DOCUMENTATION HERE
            Check if the BST is empty.
            Returns: True if tree has no nodes, else False 
        """
        return self.__root == None
    

    def getRoot(self):
        """ GETROOT DOCUMENTATION HERE
            Gives the root of BST.
            Returns root node of BST, else None
        """   
        return self.__root


    def search(self, goalKey):
        """ SEARCH DOCUMENTATION HERE
            Search for node with inputted key.
            Input:
                - goalkey: (any) key to search
            Returns: node if key is found, else None
        """
        return self.__searchHelp(self.__root, goalKey)
    

    def __searchHelp(self, node, goalKey):
        """ __SEARCHHELP DOCUMENTATION HERE
            A recursion to find a node containing theinputted key 
            by going through the tree from the inputted node.
            Inputs: 
                - node: (Node) The current node to start search
                - goalKey: (any) The key to be found in the tree
            Returns: node if Node containing key is found, else None
        """
        if node == None:

            return None
        
        if goalKey == node.key:

            return node 
        
        elif goalKey < node.key:

            return self.__searchHelp(node.left, goalKey)        #Goes to left node for smaller value
        
        else:

            return self.__searchHelp(node.right, goalKey)       #Goest to right node for larger value
        

    def lookup(self, goal):
        """ LOOKUP DOCUMENTATION HERE
            Look for value of input key.
            Input:
                - goal: (any) The key to look up
            Returns: value of inputted key, else None
        """
        node = self.__searchHelp(self.__root, goal)
        
        if node:

            return node.value
        
        return None
    

    def findSuccessor(self, subtreeRoot):
        """ FINDSUCCESSOR DOCUMENTATION HERE 
            Find successor of inputted node.
            Input:
                - subtreeRoot: (Node) The node to find successor
            Returns: Successor node of inputted node, else none 
        """
        return self.__findSuccessorHelp(subtreeRoot)
    
    
    def __findSuccessorHelp(self, node):
        """ __FINDSUCCESSOR DOCUMENTATION HERE 
            A iterator to find successor of inputted node.
            Input: 
                - node: (Node) The node to find successor
            Returns: Node of smallest key that is greater than inputted node
        """
        value = node

        while value.left != None:                   #Goes as far left to find node with smallest value

            value = value.left

        return value
    
    
    def delete(self, deleteKey):
        """ DELETE DOCUMENTATION HERE
            Delete inputted key from BST
            Input:
                - deleteKey: (any) The key of node to delete
            Returns: None
            Raises: Exception if there is no such key to delete
        """
        if self.search(deleteKey):
            self.__root = self.__deleteHelp(self.__root, deleteKey)         #Updates the root after deletion 
        else:
            raise Exception("Key not in tree.")
    
    def __deleteHelp(self, node, deleteKey):
        """ __DELETEHELP DOCUMENTATION HERE
            Method to help delete key from BST
            Inputs:
                - node: (Node) The current node to check to deletion
                - deleteKey: (any) The target key to delete
            Returns: node after deletion
        """
        if node == None:
            
            return None
        
        if deleteKey < node.key:

            node.left = self.__deleteHelp(node.left, deleteKey)             #Goes to left node 

        elif deleteKey > node.key:                                  

            node.right = self.__deleteHelp(node.right, deleteKey)           #Goes to right node 

        else:

            if node.left == None:                   #Goes to right if no left node

                return node.right
            
            elif node.right == None:                #Goes to left if no right node

                return node.left
            
            success = self.__findSuccessorHelp(node.right)                  #Children replace with successor
            node.key = success.key
            node.value = success.value
            node.right = self.__deleteHelp(node.right, success.key)

        return node
    

    def traverse(self) -> None:
        """ TRAVERSE DOCUMENTATION HERE
        Traverse through the BST to output the key-value pairs
        Returns: Printed key-value pairs
        """
        self.__traverseHelp(self.__root)

    def __traverseHelp(self, node) -> None:
        """ __TRAVERSEHELP DOCUMENTATION HERE
            A recursion to traverse through the BST
            Input:
                - node: (Node) The node to start the traversal
            Returns: Printed key-value pairs
        """
        if node != None:
            self.__traverseHelp(node.left)
            print(f"({node.key}, {node.value})")
            self.__traverseHelp(node.right)
            

    def __str__(self) -> str:
        """ Represent the tree as a string. Formats as 
            {(rootkey, rootval), {leftsubtree}, {rightsubtree}} """
        return self.__strHelp("", self.__root)
    
    def __strHelp(self, return_string, node) -> str:
        """ A recursive helper method to format the tree as a string. 
            Input: 
                - return_string: (string) Accumulates the final string to output
                - node: (Node) The current node to format
            Returns: A formatted string for this node. """
        # Base case - Represent an empty branch as "None"
        if node == None:
            return "None"
        # Recursively build the string to return
        # Note, this is equivalent to
        #   return "{" + node + ", " + \
        #                self.strHelp(return_string, node.left) + ", " + \
        #                self.strHelp(return_string, node.right) + "}"
        return "{{{}, {}, {}}}".format(node, 
                                       self.__strHelp(return_string, node.left), 
                                       self.__strHelp(return_string, node.right))
            

    ##############
    # NODE CLASS #
    ##############

    class __Node:
        """ Implementation of a node in a BST. Note that it is 
            private, so it cannot be accessed outside of a BST """

        def __init__(self, key, value, left=None, right=None):
            self.key = key         # The key of the root node of this tree
            self.value = value     # The value held by the root node of this tree
            self.left = left       # Points to the root of the left subtree
            self.right = right     # Points to the root of the right subtree

        def __str__(self):
            """ Represent the node as a string.
                Formats as "{key, value}" """
            return "({}, {})".format(self.key, self.value)
        
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5, "five")
    bst.insert(8, "eight")
    bst.insert(3, "three")
    bst.insert(1, "one")
    
    bst.traverse()