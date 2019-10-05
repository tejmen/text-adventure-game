# Python Text RPG
# Created by tej_men :D

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

##### Player Setup #####
class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start'
myPlayer = player()

##### Title Screen #####
def title_screen_selections():
    option = input("> ")
    if option.lower().strip() == ("play"):
        start_game() # placeholder until written
    elif option.lower().strip() == ("help"):
        help_menu()
    elif option.lower().strip() == ("quit"):
        sys.exit()
    while option.lower().strip() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
    if option.lower().strip() == ("play"):
        start_game() # placeholder until written
    elif option.lower().strip() == ("help"):
        help_menu()
    elif option.lower().strip() == ("quit"):
        sys.exit()

def title_screen():
    os.system('clear')
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('          - Play -          ')
    print('          - Help -          ')
    print('          - Quit -          ')
    print(' Copyright 2019 tejmen09    ')
    title_screen_selections()

def help_menu():
    print('############################')
    print('#           Help           #')
    print('############################')
    print('- Use ↑ arrow, ↓ arrow,     ')
    print('← arrow and → arrow         ')
    print('- Type your commands to do  ')
    print('them                        ')
    print('- Use "look" to inspect     ')
    print('something                   ')
    print(' Copyright 2019 tejmen09    ')
    title_screen()
##### MAP #####
#     1   2   3   4     PLAYER STARTS AT b2
#   -----------------
#   |   |   |   |   |  a
#   -----------------
#   |   |   |   |   |  b
#   -----------------
#   |   |   |   |   |  c
#   -----------------
#   |   |   |   |   |  d
#   -----------------


ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'up', 'west'
RIGHT = 'up', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                'b1': False, 'b2': False, 'b3': False, 'b4': False,
                'c1': False, 'c2': False, 'c3': False, 'c4': False,
                'd1': False, 'd2': False, 'd3': False, 'd4': False,
                }

zonemap = {
    'a1': {
        ZONENAME : 'Town Market',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : '', 
        DOWN : 'b1', 
        LEFT : '', 
        RIGHT : 'a2',
    }, 
    'a2': {
        ZONENAME : 'Town Entrance',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : '', 
        DOWN : 'b2', 
        LEFT : 'a1', 
        RIGHT : 'a3',
    }, 
    'a3': {
        ZONENAME : 'Town Square',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : '', 
        DOWN : 'b3', 
        LEFT : 'a2', 
        RIGHT : 'a4',
    }, 
    'a4': {
        ZONENAME : 'Town Hall',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : '', 
        DOWN : 'b4', 
        LEFT : 'a3', 
        RIGHT : '',
    }, 
    'b1': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'a1', 
        DOWN : 'c1', 
        LEFT : '', 
        RIGHT : 'b2',
    }, 
    'b2': {
        ZONENAME : 'Home',
        DESCRIPTION : 'This is your home!',
        EXAMINATION : 'Your home is the same - nothing has changed',
        SOLVED : False,
        UP : 'a2', 
        DOWN : 'c2', 
        LEFT : 'b1', 
        RIGHT : 'b3',
    }, 
    'b3': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'a3', 
        DOWN : 'c3', 
        LEFT : 'up', 
        RIGHT : 'b4',
    }, 
    'b4': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'a4', 
        DOWN : 'c4', 
        LEFT : 'b3', 
        RIGHT : '',
    }, 
    'c1': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'b1', 
        DOWN : 'd1', 
        LEFT : '', 
        RIGHT : 'c2',
    }, 
    'c2': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'b2', 
        DOWN : 'd2', 
        LEFT : 'c1', 
        RIGHT : 'c3',
    }, 
    'c3': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'b3', 
        DOWN : 'd3', 
        LEFT : 'c2', 
        RIGHT : 'c4',
    }, 
    'c4': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'b4', 
        DOWN : 'd4', 
        LEFT : 'c3', 
        RIGHT : '',
    }, 
    'd1': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'c1', 
        DOWN : '', 
        LEFT : '', 
        RIGHT : 'd2',
    }, 
    'd2': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'c2', 
        DOWN : '', 
        LEFT : 'd1', 
        RIGHT : 'd3',
    }, 
    'd3': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'c3', 
        DOWN : '', 
        LEFT : 'd2', 
        RIGHT : 'd4',
    }, 
    'd4': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'c4', 
        DOWN : '', 
        LEFT : 'd3', 
        RIGHT : '',
    },     
}


##### #####

##### GAME FUNCTIONALITY #####
def start_game():
    title_screen()




