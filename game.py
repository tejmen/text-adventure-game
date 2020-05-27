# Python Text RPG
# Created by tej_men :D)


import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100
godbool=False
##### Player Setup #####
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False
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
    elif option.lower().strip() == ('resume'):
        main_game_loop()
    elif option.lower().strip() == '/god':
        print('God mode not enabled, you cheat.')
        print('PLAY THE GAME PROPERLY YOU WEASAL!')
        godquestion = "DON'T CHEAT EVER AGAIN!"
        godanswer = input(godquestion)

        if godanswer == 'a':
            print('Hello god. Fancy seeing you here.')
            godbool = True
            title_screen()

        else:
            title_screen()
    while option.lower().strip() not in ['play', 'help', 'quit', 'resume', '/god']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower().strip() == ("play"):
            start_game() # placeholder until written
        elif option.lower().strip() == ("help"):
            help_menu()
        elif option.lower().strip() == ("quit"):
            sys.exit()
        elif option.lower().strip() == ('resume'):
            main_game_loop()
        elif option.lower().strip() == '/god':
            print('God mode not enabled, you cheat.')
            print('PLAY THE GAME PROPERLY YOU WEASAL!')
            print("DON'T CHEAT EVER AGAIN!")
            godanswer = input()
            if godanswer == 'a':
                    print('Hello god. Fancy seeing you here.')
                    godbool = True
                    title_screen()

def title_screen():
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('#         - Play -         #')
    print('#        - Resume -        #')
    print('#         - Help -         #')
    print('#         - Quit -         #')
    print('# Copyright 2019 tejmen09  #')
    title_screen_selections()

def help_menu():
    print('############################')
    print('#           Help           #')
    print('############################')
    print('- Use move command to move  ')
    print('- Type your commands to do  ')
    print('  them                      ')
    print('- Use "look" to inspect     ')
    print('  something                 ')
    print('  Copyright 2019 tejmen09   ')
    time.sleep(5)
    title_screen()

##### MAP #####
#     1   2   3   4     PLAYER STARTS AT b2
#   ---------------------
#   |   |       |   |   |  a
#   ---------------------
#   |   | Home  |   |   |  b
#   ---------------------
#   |   |       |   |   |  c
#   ---------------------
#   |   |       |   |   |  d
#   ---------------------


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
        DESCRIPTION : 'This is your Local Marketplace',
        EXAMINATION : 'There is a vague smell of fish and fresh produce.',
        SOLVED : False,
        UP : 'a1',
        DOWN : 'b1',
        LEFT : 'a1',
        RIGHT : 'a2',
    },
    'a2': {
        ZONENAME : 'Town Entrance',
        DESCRIPTION : 'This is an entrance to your Town.',
        EXAMINATION : 'The angel on the top symbolizes that your village is peaceful.',
        SOLVED : False,
        UP : 'a2',
        DOWN : 'b2',
        LEFT : 'a1',
        RIGHT : 'a3',
    },
    'a3': {
        ZONENAME : 'Town Square',
        DESCRIPTION : 'This is your Town Square.',
        EXAMINATION : 'There is a wishing well in the middle.',
        SOLVED : False,
        UP : 'a3',
        DOWN : 'b3',
        LEFT : 'a2',
        RIGHT : 'a4',
    },
    'a4': {
        ZONENAME : 'Town Hall',
        DESCRIPTION : 'This is where the mayor lives',
        EXAMINATION : 'Mum said "This Building has a prison for baddies!"',
        SOLVED : False,
        UP : 'a4',
        DOWN : 'b4',
        LEFT : 'a3',
        RIGHT : 'a4',
    },
    'b1': {
        ZONENAME : 'Chest',
        DESCRIPTION : 'This is an unlocked chest!',
        EXAMINATION : 'You found a sharp sword!',
        SOLVED : False,
        UP : 'a1',
        DOWN : 'c1',
        LEFT : 'b1',
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
        ZONENAME : 'Forest',
        DESCRIPTION : 'This is an oak forest.',
        EXAMINATION : 'This forest has a crossway so you can go any way you want',
        SOLVED : False,
        UP : 'a3',
        DOWN : 'c3',
        LEFT : 'up',
        RIGHT : 'b4',
    },
    'b4': {
        ZONENAME : '???',
        DESCRIPTION : 'This is an old Building.',
        EXAMINATION : 'There is a button and a circle on the floor.',
        SOLVED : False,
        UP : 'a4',
        DOWN : 'c4',
        LEFT : 'b3',
        RIGHT : '',
    },
    'c1': {
        ZONENAME : '???',
        DESCRIPTION : 'This is an old Building.',
        EXAMINATION : 'There is a button and a circle on the floor.',
        SOLVED : False,
        UP : 'b1',
        DOWN : 'd1',
        LEFT : 'c1',
        RIGHT : 'c2',
    },
    'c2': {
        ZONENAME : 'Forest',
        DESCRIPTION : 'This is an ash forest.',
        EXAMINATION : 'This forest has a crossway so you can go any way you want',
        SOLVED : False,
        UP : 'b2',
        DOWN : 'd2',
        LEFT : 'c1',
        RIGHT : 'c3',
    },
    'c3': {
        ZONENAME : 'Forest',
        DESCRIPTION : 'This is a birch forest.',
        EXAMINATION : 'This forest has a crossway so you can go any way you want.',
        SOLVED : False,
        UP : 'b3',
        DOWN : 'd3',
        LEFT : 'c2',
        RIGHT : 'c4',
    },
    'c4': {
        ZONENAME : 'Dungeon',
        DESCRIPTION : 'This is a dangerous Dungeon.',
        EXAMINATION : 'This Dungeon has dangers. Mum said to stay away from dangerous places.',
        SOLVED : False,
        UP : 'b4',
        DOWN : 'd4',
        LEFT : 'c3',
        RIGHT : 'c4',
    },
    'd1': {
        ZONENAME : 'Beach',
        DESCRIPTION : 'This is a rocky beach',
        EXAMINATION : 'This beach has lots of seaweed.',
        SOLVED : False,
        UP : 'c1',
        DOWN : 'd1',
        LEFT : 'd1',
        RIGHT : 'd2',
    },
    'd2': {
        ZONENAME : 'Beach',
        DESCRIPTION : 'This is a white, sandy Beach.',
        EXAMINATION : 'This beach has lots of children playing on it.',
        SOLVED : False,
        UP : 'c2',
        DOWN : 'd2',
        LEFT : 'd1',
        RIGHT : 'd3',
    },
    'd3': {
        ZONENAME : 'Dungeon',
        DESCRIPTION : 'This is a dangerous Dungeon.',
        EXAMINATION : 'This Dungeon has dangers. Mum said to stay away from dangerous places.',
        SOLVED : False,
        UP : 'c3',
        DOWN : 'd2',
        LEFT : 'd2',
        RIGHT : 'd4',
    },
    'd4': {
        ZONENAME : 'End Portal',
        DESCRIPTION : 'This is where you go if you want to stop exploring.',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'c4',
        DOWN : 'd4',
        LEFT : 'd3',
        RIGHT : 'd4',
    },
}


##### GAME INTERACTIVITY #####
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + zonemap[myPlayer.location][ZONENAME] + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] +' #')
    print('#' * (4 + len(myPlayer.location)))

def prompt():
    print('\n' + '===============================')
    print('What would you like to do?')
    print("(You can 'move', 'quit' or 'look')")
    action = input('> ')
    acceptable_actions = ['move', 'quit', 'look', '/god']
    while action.lower() not in acceptable_actions:
        print('Unknown action, try again.\n')
        action = input('> ')
    if action.lower().strip() == 'quit':
        sys.exit()
    if action.lower().strip() == 'move':
        player_move()
    elif action.lower().strip() ==  'look':
        player_examine()
    elif action.lower().strip() == '/god':
        print('God mode not enabled, you cheat.')
        print('PLAY THE GAME PROPERLY YOU WEASAL!')
        print("DON'T CHEAT EVER AGAIN!")
def player_move():

    ask = 'Where would you like to move to?\n'
    print("You can move 'up', 'down', 'left' or 'right'.")
    dest = input(ask)
    if dest == 'up' or dest == 'north':
        print('I will move up now')
        print(zonemap[myPlayer.location][UP])
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest == 'down' or dest == 'south':
        print('I will move down now')
        print(zonemap[myPlayer.location][DOWN])
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest == 'left' or dest == 'west':
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest == 'right' or dest == 'east':
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest == 'tp': #and godbool == True:
        teleport()

def movement_handler(destination):
    print('\n'+ 'You have moved to ' + destination + '.')
    myPlayer.location = destination
    print_location()

def player_examine():
    if myPlayer.location == 'd4':
        title_screen();

    print(zonemap[myPlayer.location][EXAMINATION])



##### GAME FUNCTIONALITY #####
def start_game():
    setup_game()

def main_game_loop():
    while myPlayer.game_over is False:
        prompt()

def setup_game():
    ### NAME COLLECTING ###
    question1 = 'What is your name young traveller?\n'
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name
    ### JOB HANDELLING ###
    question2 = 'What is will your role be ' + player_name +'?\n'
    question2added = '(You can be a Fighter, Wizard or healer)\n'
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("> ").lower()
    valid_jobs = ['fighter', 'wizard', 'healer']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print('you are now a ' + player_job + '!\n')
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print('you are now a ' + player_job + '!\n')
    ### PLAYER STATS ###
    if myPlayer.job == 'fighter':
        myPlayer.hp = 120
        myPlayer.mp = 20
    elif myPlayer.job == 'wizard':
        myPlayer.hp = 40
        myPlayer.mp = 120
    elif myPlayer.job == 'healer':
        myPlayer.hp = 60
        myPlayer.mp = 60

    ### INTRODUCTION ###
    question3 = 'Welcome ' + player_name +' the ' + player_job + '.\n'
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    speech1 = 'Welcome to this fanatasy world!\n'
    speech2 = 'I hope you enjoy!\n'
    speech3 = 'Just dont get lost...\n'
    speech4 = '(Cough, Cough)\n'

    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)


    print('############################')
    print('#       Lets Jump In!      #')
    print('############################')
    main_game_loop()
def teleport():
    print('Where do you want to go god?')
    qa = input('_')
    myPlayer.location = qa
    destination = myPlayer.location
    movement_handler(destination)


title_screen()
