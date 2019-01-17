"""
 This is the main file.

This will be the main file for the CLI and all game logic.

"""
import random
import datetime
from colors import print_red


def welcome_screen():
    """
    welcome_screen initialize the game interface.
    First time intro the game to the users.
    """
    players = []
    player_initial = ""
    num_of_players = int(input("How many players (2-4): "))
    if not num_of_players or num_of_players < 2 or num_of_players > 4:
        print_red(f"Seriously?, {num_of_players} players, Haha!")
    else:
        for i in range(1, num_of_players + 1):
            player_initial = str(input(f"Player initial for the player {i}: "))
            players.append(player_initial.upper())
        return players
    return "Try again, Bye Bye!!"
# Test if it works
# print(welcome_screen())

def dice_roll():
    """
    dice_roll Dice rolling for players.
    
    Generates a randum number between 1 to 6. Needed to move users' position on the grid.
    
    """
    while True:
        wish = int(input("Roll the dice by pressing any number (1 - 6) that you wish to get: "))
        if not wish or wish < 1 or wish > 6:
            print_red("You can't get both chichi and papa, TRY A VALID NUMBER")
            continue
        else:
            break
    return wish
# Test if it works
# print(dice_roll())
