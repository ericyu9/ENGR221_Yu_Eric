"""
Author: Prof. Alyssa
The Controller of the game, including handling key presses
(and AI in the next assignment). You will update this file.

Adapted from HMC CS60

Author: Eric Yu
Date: December 8, 2024
Description: This code implements the keybinds to move the snake in the game.
"""

from preferences import Preferences
from gameData import GameData
from boardDisplay import BoardDisplay

import pygame
from enum import Enum
from queue import Queue

class Controller():
    def __init__(self):
        # The current state of the board
        self.__data = GameData()
        # The display
        self.__display = BoardDisplay()
        # How many frames have passed
        self.__numCycles = 0

        self.__paused = False               #Pause state of game

        # Attempt to load any sounds and images
        try:
            pygame.mixer.init()
            self.__audioEat = pygame.mixer.Sound(Preferences.EAT_SOUND)
            self.__display.headImage = pygame.image.load(Preferences.HEAD_IMAGE)
        except:
            print("Problem error loading audio / images")
            self.__audioEat = None

        # Initialize the board for a new game
        self.startNewGame()
        
    def startNewGame(self):
        """ Initializes the board for a new game """

        # Place the snake on the board
        self.__data.placeSnakeAtStartLocation()

    def gameOver(self):
        """ Indicate that the player has lost """
        self.__data.setGameOver()

    def run(self):
        """ The main loop of the game """
        # Keep track of the time that's passed in the game 
        clock = pygame.time.Clock()

        # Loop until the game ends
        while not self.__data.getGameOver():
            self.checkKeypress()
            if self.__paused:
                
                clock.tick(Preferences.SLEEP_TIME)
                continue

            # Run the main behavior
            self.cycle() 
            # Sleep
            clock.tick(Preferences.SLEEP_TIME)

    def cycle(self):
        """ The main behavior of each time step """

        # Check for user input
        self.checkKeypress()
        # Update the snake state
        self.updateSnake()
        # Update the food state
        self.updateFood()
        # Increment the number of cycles
        self.__numCycles += 1
        # Update the display based on the new state
        self.__display.updateGraphics(self.__data)
        

    def checkKeypress(self):
        """ Update the game based on user input """
        # Check for keyboard input
        for event in pygame.event.get():
            # Quit the game
            if event.type == pygame.QUIT:
                self.gameOver()
            # Change the snake's direction based on the keypress
            elif event.type == pygame.KEYDOWN:
                if event.key in self.Keypress.UP.value:

                    self.__data.setDirectionNorth()         

                elif event.key in self.Keypress.DOWN.value:

                    self.__data.setDirectionSouth()

                elif event.key in self.Keypress.LEFT.value:
                    
                    self.__data.setDirectionWest()

                elif event.key in self.Keypress.RIGHT.value:

                    self.__data.setDirectionEast()

                elif event.key in self.Keypress.REVERSE.value:

                    self.reverseSnake()

                elif event.key in self.Keypress.AI.value:

                    self.__data.toggleAIMode()

                elif event.key in self.Keypress.PAUSE.value:

                    self.togglePause()


    def updateSnake(self):
        """ Move the snake forward one step, either in the current 
            direction, or as directed by the AI """

        if self.__numCycles % Preferences.REFRESH_RATE == 0:
            try:
                # Find the next cell
                if self.__data.inAIMode():
                    nextCell = self.getNextCellFromBFS()
                else:
                    nextCell = self.__data.getNextCellInDir()
            
            except Exception as e:
                print(f"Failed to advance snake: {e}")
            
            print(f"Next cell: {nextCell}")  # Debugging

            # Move the snake to the next cell
            self.advanceSnake(nextCell)

        
    def advanceSnake(self, nextCell):
        """ Update the state of the world to move the snake's head to the given cell """
    
        print(f"Advancing snake to cell: {nextCell}")

        # If the snake runs into a wall or itself
        if nextCell.isWall() or nextCell.isBody():

            self.gameOver()
    
        # If the snake eats food
        elif nextCell.isFood():

            self.__data.eatFood(nextCell)               #Update the data for food being eaten
            nextCell.becomeHead()                       #Marks next cell has the head
            self.__data.getSnakeHead().becomeBody()     #Old head becomes a body
            self.__data.addHead(nextCell)               #New head added to the list

        
        elif nextCell.isEmpty():

            nextCell.becomeHead()                       
            self.__data.getSnakeHead().becomeBody()
            self.__data.addHead(nextCell)


            tail = self.__data.removeTail()             #Remove tail
            tail.becomeEmpty()                          #Removed tail cell become empty  

    def updateFood(self):
        """ Add food every FOOD_ADD_RATE cycles or if there is no food """
        if self.__data.noFood() or (self.__numCycles % Preferences.FOOD_ADD_RATE == 0):
            self.__data.addFood()

    def getNextCellFromBFS(self):
        """ Uses BFS to search for the food closest to the head of the snake.
            Returns the *next* step the snake should take along the shortest path
            to the closest food cell. """
        
        try:
            self.__data.resetCellsForSearch()   #Tiles to search

            cellsToSearch = Queue()             #Queue to search tiles

            head = self.__data.getSnakeHead()   #Add the head to queue
            head.setAddedToSearchList()
            cellsToSearch.put(head)

            while not cellsToSearch.empty():
                current = cellsToSearch.get()

                if current.isFood():
                    return self.getFirstCellInPath(current)

                for neighbor in self.__data.getNeighbors(current):      #Searches the neighboring tiles
                    if not neighbor.alreadyAddedToSearchList() and not neighbor.isWall() and not neighbor.isBody():

                        neighbor.setAddedToSearchList()
                        neighbor.setParent(current)
                        cellsToSearch.put(neighbor)

            return self.__data.getRandomNeighbor(head)
    
        except Exception as e:

            print(f"BFS Error: {e}")

            raise

    def getFirstCellInPath(self, food_Cell):
        """ Trace back food to head."""
        while food_Cell.getParent():          #Traces back path until it reaches the head
            if food_Cell.getParent() == self.__data.getSnakeHead():

                return food_Cell
            
            food_Cell = food_Cell.getParent()
            
        return food_Cell 

    
    def reverseSnake(self):
        """ Reverses the direction of the snake, switching the head and tail. """
        snake_cells = self.__data._GameData__snakeCells

        snake_cells.reverse()

        for i, cell in enumerate(snake_cells):
            if i == 0: 
                cell.becomeHead()
            else:
                cell.becomeBody()

        new_head = snake_cells[0]   
        neck = snake_cells[1]

        if new_head.getRow() < neck.getRow():

            self.__data.setDirectionNorth()

        elif new_head.getRow() > neck.getRow():

            self.__data.setDirectionSouth()

        elif new_head.getCol() < neck.getCol():

            self.__data.setDirectionWest()

        elif new_head.getCol() > neck.getCol():

            self.__data.setDirectionEast()

    def togglePause(self):
        """ Toggles the pause state of the game """
        self.__paused = not self.__paused
        if self.__paused:
            print("Game Paused")
        else:
            print("Game Resumed")

    def playSound_eat(self):
        """ Plays an eating sound """
        if self.__audioEat:
            pygame.mixer.Sound.play(self.__audioEat)
            pygame.mixer.music.stop()

    class Keypress(Enum):
        """ An enumeration (enum) defining the valid keyboard inputs 
            to ensure that we do not accidentally assign an invalid value.
        """
        UP = pygame.K_i, pygame.K_UP        # i and up arrow key
        DOWN = pygame.K_k, pygame.K_DOWN    # k and down arrow key
        LEFT = pygame.K_j, pygame.K_LEFT    # j and left arrow key
        RIGHT = pygame.K_l, pygame.K_RIGHT  # l and right arrow key
        REVERSE = pygame.K_r,               # r
        AI = pygame.K_a,                    # a
        PAUSE = pygame.K_p,                 # p


if __name__ == "__main__":
    Controller().run()