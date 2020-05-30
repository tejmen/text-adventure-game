# Python Text RPG
# Created by tej_men
#     \
# (:D)-<
#     /


import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100
godbool = '1'
##### Player Setup #####
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.ap = 0
        self.heal = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False
        self.inventory = ''
        self.weapon = ''
        self.xp = 0
myPlayer = player()

class Gslime:
    def __init__(self):
        self.hp = 300
        self.ap = 20
GreenS = Gslime()


##### Title Screen #####
def title_screen_selections():
    option = input("> ")
    if option.lower().strip() == ("play"):
        start_game() # placeholder until written
    elif option.lower().strip() == ("help"):
        help_menu()
    elif option.lower().strip() == ("quit"):
        print('You have')
        print(myPlayer.xp)
        sys.exit()
    elif option.lower().strip() == ('resume'):
        main_game_loop()
    elif option.lower().strip() == ("acknowledgements"):
        acknowledgements_menu()
    elif option.lower().strip() == '/god':
        print('God mode not enabled, you cheat.')
        print('PLAY THE GAME PROPERLY YOU WEASAL!')
        godquestion = "DON'T CHEAT EVER AGAIN!"
        godanswer = input(godquestion)

        if godanswer == 'a':
            print('Hello god. Fancy seeing you here.')
            godbool = 'yes'
            title_screen()

        else:
            title_screen()
    while option.lower().strip() not in ['play', 'help', 'quit', 'resume', '/god', 'acknowledgements']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower().strip() == ("play"):
            start_game() # placeholder until written
        elif option.lower().strip() == ("help"):
            help_menu()
        elif option.lower().strip() == ("quit"):
            print('You have')
            print(myPlayer.xp)
            sys.exit()
        elif option.lower().strip() == ('resume'):
            main_game_loop()
        elif option.lower().strip() == ("acknowledgements"):
            acknowledgements_menu()
        elif option.lower().strip() == '/god':
            print('God mode not enabled, you cheat.')
            print('PLAY THE GAME PROPERLY YOU WEASAL!')
            print("DON'T CHEAT EVER AGAIN!")
            godanswer = input()
            if godanswer == 'a':
                    print('Hello god. Fancy seeing you here.')
                    godbool = 'yes'
                    title_screen()

def title_screen():
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('#         - Play -         #')
    print('#        - Resume -        #')
    print('#         - Help -         #')
    print('#   - Acknowledgements -   #')
    print('#         - Quit -         #')
    print('# Copyright 2019 tejmen09  #')
    title_screen_selections()

def help_menu():
    print('###############################')
    print('#            Help             #')
    print('# • Use move command to move  #')
    print('# • Type your commands to do  #')
    print('#   them                      #')
    print('# • Use "look" to inspect     #')
    print('#   something                 #')
    print('#   Copyright 2019 tejmen09   #')
    print('###############################')
    time.sleep(5)
    title_screen()
def acknowledgements_menu():
    print('###############################')
    print('#       Acknowledgements      #')
    print('# Beta Tested By:             #')
    print('# • Manas Mengle              #')
    print('# • Pranot Mengle             #')
    print('# • Mennakshi Mengle          #')
    print('# Helped By:                  #')
    print('# • Manas Mengle              #')
    print('# • Pranot Mengle             #')
    print('# Copyright 2019 Tejas Mengle #')
    print('###############################')
    time.sleep(5)
    title_screen()



##### MAP #####
#     1     2    3    4     PLAYER STARTS AT b2
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
        EXAMINATION : 'The key is already in the Chest lock.',
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
        SOLVED : True,
        UP : 'a3',
        DOWN : 'c3',
        LEFT : 'b2',
        RIGHT : 'b4',
    },
    'b4': {
        ZONENAME : '???',
        DESCRIPTION : 'This is an old Building.',
        EXAMINATION : 'There is a button and a glowing circle on the floor.',
        SOLVED : False,
        UP : 'a4',
        DOWN : 'c4',
        LEFT : 'b3',
        RIGHT : 'b4',
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
        SOLVED : True,
        UP : 'b2',
        DOWN : 'd2',
        LEFT : 'c1',
        RIGHT : 'c3',
    },
    'c3': {
        ZONENAME : 'Forest',
        DESCRIPTION : 'This is a birch forest.',
        EXAMINATION : 'This forest has a crossway so you can go any way you want.',
        SOLVED : True,
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
        EXAMINATION : 'This is a way to go to the main menu.',
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
    print("(You can 'move', 'quit', 'look', 'xp' or 'act')")
    action = input('> ')
    acceptable_actions = ['move', 'quit', 'look', '/god', 'acceptable_actions', 'act', 'xp']
    while action.lower() not in acceptable_actions:
        print('Unknown action, try again.\n')
        action = input('> ')
    if action.lower().strip() == 'quit':
        print('You have')
        print(myPlayer.xp)
        sys.exit()
    if action.lower().strip() == 'move':
        player_move()
    elif action.lower().strip() ==  'look':
        player_examine()
    elif action.lower().strip() == '/god':
        print('God mode not enabled, you cheat.')
        print('PLAY THE GAME PROPERLY YOU WEASAL!')
        print("DON'T CHEAT EVER AGAIN!")
    elif action.lower().strip() == 'acceptable_actions':
        print('You have found an easter egg.')
        print("Don't tell anyone." + " ;)")
    elif action.lower().strip() == 'act':
        player_act()
    elif action.lower().strip() == 'xp':
        print('You have')
        print(myPlayer.xp)

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
    #if godbool == 'yes':
    if dest == 'tp':
        print('Where do you want to go god?')
        qa = input('_')
        myPlayer.location = qa
        destination = myPlayer.location
        movement_handler(destination)

def movement_handler(destination):
    print('\n'+ 'You have moved to ' + destination + '.')
    myPlayer.location = destination
    print_location()

def player_examine():
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
        print('Unknown action, try again.\n')
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print('you are now a ' + player_job + '!\n')
    ### PLAYER STATS ###
    if myPlayer.job == 'fighter':
        myPlayer.hp = 120
        myPlayer.ap = 50
        myPlayer.weapon = 'sword'
    elif myPlayer.job == 'wizard':
        myPlayer.hp = 300
        myPlayer.ap = 30
        myPlayer.weapon = 'staff'
    elif myPlayer.job == 'healer':
        myPlayer.hp = 200
        myPlayer.ap = 40
        myPlayer.heal = 40
        myPlayer.weapon = 'magic book'

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

def player_act():
    if zonemap[myPlayer.location][SOLVED] == False:
        if myPlayer.location == 'b4':
            myPlayer.location = 'c1'
            zonemap[myPlayer.location][ZONENAME] = 'Telporter'
            destination = myPlayer.location
            movement_handler(destination)
        elif myPlayer.location == 'c1':
            myPlayer.location = 'b4'
            zonemap[myPlayer.location][ZONENAME] = 'Telporter'
            destination = myPlayer.location
            movement_handler(destination)
        elif myPlayer.location == 'd4':
            title_screen()
        elif myPlayer.location == 'a1':
            zonemap[myPlayer.location][SOLVED] = True
            print('I was going to buy an apple, but I dont have any money.')
        elif myPlayer.location == 'a2':
            zonemap[myPlayer.location][SOLVED] = True
            print('There is nothing you can do ' + myPlayer.name + ' the ' + myPlayer.job)
        elif myPlayer.location == 'a3':
            zonemap[myPlayer.location][SOLVED] = True
            print('The mayoral election are going on. I wish I could vote, but I am too young.')
        elif myPlayer.location == 'a4':
            zonemap[myPlayer.location][SOLVED] = True
            print("There is a weird smell of rotten eggs inside. I'm not going inside!")
        elif myPlayer.location == 'b1':
            zonemap[myPlayer.location][SOLVED] = True
            print('You pick up the ' + myPlayer.weapon)
            myPlayer.inventory = myPlayer.weapon
        elif myPlayer.location == 'b2':
            zonemap[myPlayer.location][SOLVED] = True
            print1 = 'You take a nap'
            for character in print1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(1)
        elif myPlayer.location == 'b3':
            zonemap[myPlayer.location][SOLVED] = True
            print('There is nothing you can do ' + myPlayer.name + ' the ' + myPlayer.job)
        elif myPlayer.location == 'c2':
            zonemap[myPlayer.location][SOLVED] = True
            print('There is nothing you can do ' + myPlayer.name + ' the ' + myPlayer.job)
        elif myPlayer.location == 'c3':
            zonemap[myPlayer.location][SOLVED] = True
            print('There is nothing you can do ' + myPlayer.name + ' the ' + myPlayer.job)
        elif myPlayer.location == 'c4':
            turn_based_combat()
        elif myPlayer.location == 'd1':
            zonemap[myPlayer.location][SOLVED] = True
            print('This beach is too rocky and full of seaweed to do anything ' + myPlayer.name + ' the ' + myPlayer.job)
        elif myPlayer.location == 'd2':
            zonemap[myPlayer.location][SOLVED] = True
            print('this beach is so sandy that...')
            print1 = 'you take a nap.'
            for character in print1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(1)
        elif myPlayer.location == 'd3':
            turn_based_combat()
    else:
        print('This place has already been excavated...')
        print('BY YOU!')
def turn_based_combat():
    print('##########################################')
    print('# A Green Slime appeared out of the dark #')
    print('##########################################')
    while GreenS.hp > 0:
        print('What would you like to do?')
        print("(You can type 'attack' to attack the Green slime.)")
        attack = input('> ')
        acceptable_attack = ['attack','kill', 'heal']
        while attack.lower().strip() not in acceptable_attack:
            print('Unknown action, try again.\n')
            attack = input('> ')
            if attack.lower().strip() == 'attack':
                GreenS.hp = GreenS.hp - myPlayer.ap
                print("The green slime's health is ")
                print(GreenS.hp)
            elif attack.lower().strip() == 'kill':
                GreenS.hp = 0
                print("The green slime's health is ")
                print(GreenS.hp)
        if attack.lower().strip() == 'attack':
            GreenS.hp = GreenS.hp - myPlayer.ap
            if GreenS.hp < 0:
                GreenS.hp = 0
                print("The green slime's health is ")
                print(GreenS.hp)
            else:
                print("The green slime's health is ")
                print(GreenS.hp)
        elif attack.lower().strip() == 'kill':
            GreenS.hp = 0
            print("The green slime's health is ")
            print(GreenS.hp)
        if attack.lower().strip() == 'heal':
            if myPlayer.job == 'healer':
                myPlayer.hp = myPlayer.hp + myPlayer.heal
                if myPlayer.hp > 200:
                    myPlayer.hp = 200
                text3 = 'You have '
                text4 = 'health now.\n'
                for character in text3:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.1)
                print(myPlayer.hp)
                time.sleep(1)
                for character in text4:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.1)
            else:
                print("You can't heal. You're not a healer.")
        if GreenS.hp > 0:
            print('\n################################')
            print('# The Green Slime attacked you.#')
            print('################################')
            myPlayer.hp = myPlayer.hp - GreenS.ap
            text = 'You have '
            text2 = 'health left.\n'
            for character in text:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.1)
            print(myPlayer.hp)
            for character in text2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.1)
    print('####################################')
    print('# You have defeated a green slime. #')
    print('#     You have gained 100 XP.      #')
    print('####################################')
    myPlayer.xp = 100
    GreenS.hp = 300
    zonemap[myPlayer.location][SOLVED] = True
    main_game_loop()

title_screen()
