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


##### GAME FUNCTIONALITY #####
def start_game():
    




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
        ZONENAME = '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'up', 'west'
        RIGHT = 'up', 'east'
    },
    'a2': {
        ZONENAME = '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'up', 'west'
        RIGHT = 'up', 'east'
    },
    'a3': {
        ZONENAME = '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'up', 'west'
        RIGHT = 'up', 'east'
    },
    'a4': {
        ZONENAME = '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'up', 'west'
        RIGHT = 'up', 'east'
    },
    'b1': {
        ZONENAME = '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'up', 'west'
        RIGHT = 'up', 'east'
    },
    'b2': {
        ZONENAME = 'Home',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'up', 'west'
        RIGHT = 'up', 'east'
    },
    'b3': {
        ZONENAME = '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'up', 'west'
        RIGHT = 'up', 'east'
    },
    'b4': {
        ZONENAME = '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'up', 'west'
        RIGHT = 'up', 'east'
    },
    'c1': {
        ZONENAME = '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'up', 'west'
        RIGHT = 'up', 'east'
    },
    'c2': {
        ZONENAME = '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'up', 'west'
        RIGHT = 'up', 'east'
    },
    'c3': {
        ZONENAME = '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'up', 'west'
        RIGHT = 'up', 'east'
    },
    'c4': {
        ZONENAME = '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'up', 'west'
        RIGHT = 'up', 'east'
    },
    'd1': {
        ZONENAME = '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'up', 'west'
        RIGHT = 'up', 'east'
    },
    'd2': {
        ZONENAME = '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'up', 'west'
        RIGHT = 'up', 'east'
    },
    'd3': {
        ZONENAME = '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'up', 'west'
        RIGHT = 'up', 'east'
    },
    'd4': {
        ZONENAME = '',
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'up', 'west'
        RIGHT = 'up', 'east'
    },
}






































