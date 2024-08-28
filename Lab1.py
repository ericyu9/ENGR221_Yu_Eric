"""
Author: Eric Yu
File Name: Lab1.py
Description: Contains code that prints the phrase "Go Gators!" and rock paper scissors program.
Date: August 28, 2024
"""
print ("Go gators!") #Prints message when program is run

import random # imports the library named random
def rps():
    """This plays a game of rock-paper-scissors
    (or a variant of that game)
    Arguments: none (prompted text doesn't count as an argument)
    Results: none (printing doesn't count as a result)
    """
    user = input("Choose your weapon: ")
    comp = random.choice(['rock', 'paper', 'scissors']) #Randomizes the move the computer makes


    print('The user (you) chose', user)
    print('The computer (I) chose', comp)

    if user == 'rock' and comp == 'scissors': #If statements check the moves of player and computer to determine who wins
        print('You won!')

    elif user == 'rock' and comp == 'paper':
        print('I won!')

    elif user == 'rock' and comp == 'rock':
        print('Its a tie!')

    elif user == 'paper' and comp == 'scissors':
        print('I won!')

    elif user == 'paper' and comp == 'rock':
        print('You won!')

    elif user == 'paper' and comp == 'paper':
        print('Its a tie!')

    elif user == 'scissors' and comp == 'rock':
        print('I won!')

    elif user == 'scissors' and comp == 'paper':
        print('You won!')

    elif user == 'scissors' and comp == 'scissors':
        print('Its a tie!')

rps()
