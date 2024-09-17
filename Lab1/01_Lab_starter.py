
#
# Name: 
# Lab1.py
#

# Code from 4e. to print “go gators” goes here

import random          # imports the library named random

def rps():
    """This plays a game of rock-paper-scissors
       (or a variant of that game)
       Arguments: none     (prompted text doesn't count as an argument)
       Results: none       (printing doesn't count as a result)
    """
    user = input("Choose your weapon: ")
    comp = random.choice(['rock', 'paper', 'scissors'])
    print()

    print('The user (you)   chose', user)
    print('The computer (I) chose', comp)
    print()

    if user == 'rock' and comp == 'scissors':
        print('Ha! I actually chose paper, which annihilates your rock.')

    elif user == 'rock' and comp == 'paper':
        print('I won! Your rock is dust!')
   

    print("Better luck next time...")

rps()