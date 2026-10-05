# Snake Water Gun:
# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors"
# The gun beats the snake, the water beats the gun, and the snake beats the water.
# Write a python program to create a Snake Water Gun game in python using if-else statements.
# Do not create any fancy GUI. Use proper functions to check for win.

Computer = "Instructions! -1 for Snake, 0 for Water and 1 for Gun"
print(Computer)

import random

Computer = [-1, 0, 1]
x = random.choice(Computer)

Player = int(input("Choose one at a time: "))

print("Computer choose", x)


def CheckWin(x, Player):
    if x == Player:
        return 0

    if x == -1 and Player == 0:
        return -1

    elif x == -1 and Player == 1:
        return 1

    if x == 1 and Player == 0:
        return 1

    elif x == 1 and Player == -1:
        return -1

    if x == 0 and Player == -1:
        return 1

    elif x == 0 and Player == 1:
        return -1


result = CheckWin(x, Player)

if result == 0:
    print("Draw")
elif result == 1:
    print("Player Wins")
elif result == -1:
    print("Computer Wins")



    
    
