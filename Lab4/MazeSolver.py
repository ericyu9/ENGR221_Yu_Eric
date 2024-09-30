"""
Author: Eric Yu
Filename: MazeSolver.py
Description: Code solves a maze using 
Date: September 29, 2024 
"""
from .SearchStructures import Stack, Queue
from .Maze import Maze

class MazeSolver:
    # Constructor
    # Inputs:
    #   maze: The maze to solve (Maze)
    #   searchStructure: The search structure class to use (Stack or Queue)
    def __init__(self, maze, searchStructure):
        self.maze = maze             # The maze to solve
        self.ss = searchStructure()  # Initialize a searchStructure object

    def tileIsVisitable(self, row:int, col:int) -> bool:
        # ~~~~~~~~

        if row < 0 or row >= self.maze.num_rows or col < 0 or col >= self.maze.num_cols:
            return False    #Checks f row or column is out of bounds 
        
        Tile = self.maze.contents[row][col]     #Tile set to coordinates
        
        if Tile.visited():                      #Checks if the tile has been visited
            return False
        
        elif Tile.isWall():                     #Checks if the tile is a wall
            return False
        
        else:
            return True
        

        # ~~~~~~~~
        
        

    def solve(self):
        # ~~~~~~~~
        start = self.maze.start                 #Sets the starting tile of maze
        start.visit()                           #Marks start tile as visited
        self.ss.add(start)                      #Adds the start tile to search structure
        

        while not self.ss.isEmpty():                                    #Loop that runs while search structure has items
            current = self.ss.remove()                                  #Removes the current tile from search structures

            if current == self.maze.goal:                               #Checks if the current tile is matching the goal tile
                return 

            for direction in [(-1,0),(1,0),(0,-1),(0,1)]:               #Explore directions in North, South, East, West
                row2 = current.getRow() + direction[0]                  #Finds the row value next to current tile
                col2 = current.getCol() + direction[1]                  #Finds the column value next to current tile

                if self.tileIsVisitable(row2, col2):                    #Checks the tiles around if they are visitable
                    next_tile = self.maze.contents[row2][col2]          #Gets the next tile
                    next_tile.visit()                                   #Mark the next tile as visited
                    next_tile.setPrevious(current)                      #Mark the previous tile to backtrack
                    self.ss.add(next_tile)                              #Adds the next tile to search structure
        # ~~~~~~~~
        

     # Add any other helper functions you might want here

    def getPath(self):
        # ~~~~~~~~
        path = []                                   #Initialize a list to store the goal path
        current = self.maze.goal                    #Starts from goal tile

        while current is not None:                  #Loops while there are previous tiles to visit
            path.append(current)                    #Add current tile to path
            current = current.getPrevious()         #Move to previous tile 
        path.reverse()                              #Reverses the path to be from start to goal

        return path                                 #Returns the path to goal
        # ~~~~~~~~
         

    # Print the maze with the path of the found solution
    # from Start to Goal. If there is no solution, just
    # print the original maze.
    def printSolution(self):
        # Get the solution for the maze from the maze itself
        solution = self.getPath()
        # A list of strings representing the maze
        output_string = self.maze.makeMazeBase()
        # For all of the tiles that are part of the path, 
        # mark it with a *
        for tile in solution:
            output_string[tile.getRow()][tile.getCol()] = '*'
        # Mark the start and goal tiles
        output_string[self.maze.start.getRow()][self.maze.start.getCol()] = 'S'
        output_string[self.maze.goal.getRow()][self.maze.goal.getCol()] = 'G'

        # Print the output string
        for row in output_string:
            print(row)

   

if __name__ == "__main__":
    # The maze to solve
    maze = Maze(["____",
                 "S##E",
                 "__#_",
                 "____"])
    # Initialize the MazeSolver to be solved with a Stack
    solver = MazeSolver(maze, Stack)
    # Solve the maze
    solver.solve()
    # Print the solution found
    solver.printSolution()