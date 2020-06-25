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
from random import randrange
import map
import math

random_attacker = (random.randint(1,3))
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
        self.inventory = []
        self.weapon = ''
        self.xp = 0
myPlayer = player()

class Gslime:
    def __init__(self):
        self.hp = 300
        self.ap = 20
        self.xp = 100
        self.max = 300
GreenS = Gslime()
class Zomboy:
    def __init__(self):
        self.hp = 500
        self.ap = 40
        self.xp = 500
        self.max = 500
zombie = Zomboy()
class Skelemob:
    def __init__(self):
        self.hp = 500
        self.ap = 40
        self.xp = 300
        self.max = 500
skeleton = Skelemob()
class Sword:
    def __init__(self):
        self.name = "Soldier's Broadsword"
        self.ap = 100
class Staff:
    def __init__(self):
        self.name = "Wizard's Arcane Staff"
        self.ap = 75
class MagicBook:
    def __init__(self):
        self.name = "Healer's Book of Magic"
        self.ap = 50
class Knife:
    def __init__(self):
        self.name = "Traveller's Knife"
        self.ap = 80

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
        print('xp.')
        print('###############')
        print('#  GOODBYE!!  #')
        print('###############')
        time.sleep(0.5)
        sys.exit()
    elif option.lower().strip() == ('resume'):
        main_game_loop()
    elif option.lower().strip() == ("acknowledgements"):
        acknowledgements_menu()
    elif option.lower().strip() == '/god':
        print('God mode not enabled, you cheat.')
        print('PLAY THE GAME PROPERLY YOU WEASEL!')
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
            print('xp.')
            print('###############')
            print('#  GOODBYE!!  #')
            print('###############')
            time.sleep(0.5)
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
    print('# • Type "move" command to    #')
    print('#   move                      #')
    print('# • Type your commands to do  #')
    print('#   them                      #')
    print('# • Type "look" to inspect    #')
    print('#   something                 #')
    print('# • Type "act" to do what you #')
    print('#   can on your place         #')
    print('# • If you find a Dungeon,    #')
    print('#  please help to excavate it #')
    print('# • Find more weapons to kill #')
    print('#  monsters                   #')
    print('# • Help villagers for reward #')
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
    time.sleep(3)
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
DIALOGUE = 'dialogue'
ACTION = 'action'


##### GAME INTERACTIVITY #####
def print_location():
    print('\n' + ('#' * (4 + len(map.zonemap[myPlayer.location][DESCRIPTION]))))
    print('# ' + map.zonemap[myPlayer.location][ZONENAME] + ' ' * (len(map.zonemap[myPlayer.location][DESCRIPTION]) - len(map.zonemap[myPlayer.location][ZONENAME])) +' #')
    print('# ' + map.zonemap[myPlayer.location][DESCRIPTION] +' #')
    print('#' * (4 + len(map.zonemap[myPlayer.location][DESCRIPTION])))

def prompt():
    print('\n' + '===============================')
    print('What would you like to do?')
    print("(You can 'move', 'quit', 'look', 'xp', 'talk', 'switchweapon', 'stats' or 'act')")
    action = input('> ')
    acceptable_actions = ['move', 'quit', 'look', '/god', 'acceptable_actions', 'act', 'xp', 'talk', 'switchweapon', 'stats']
    while action.lower() not in acceptable_actions:
        print('Unknown action, try again.\n')
        action = input('> ')
    if action.lower().strip() == 'quit':
        print('You have')
        print(myPlayer.xp)
        print('xp.')
        print('###############')
        print('#  GOODBYE!!  #')
        print('###############')
        time.sleep(0.5)
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
        print('xp.')
    elif action.lower().strip() == 'talk':
        player_talk()
    elif action.lower().strip() == 'switchweapon':
        switch_weapon()
    elif action.lower().strip() == 'stats':
        stats()
def player_move():
    ask = 'Where would you like to move to?\n'
    print("You can move 'up', 'down', 'left' or 'right'.")
    dest = input(ask)
    if dest == 'up' or dest == 'north':
        if 'a' in myPlayer.location:
            print("You have reached the end of the map. Don't go up.")
        else:
            print(map.zonemap[myPlayer.location][UP])
            destination = map.zonemap[myPlayer.location][UP]
            movement_handler(destination)
    elif dest == 'down' or dest == 'south':
        if 'd' in myPlayer.location:
            print("You have reached the end of the map. Don't go down.")
        else:
            print(map.zonemap[myPlayer.location][DOWN])
            destination = map.zonemap[myPlayer.location][DOWN]
            movement_handler(destination)
    elif dest == 'left' or dest == 'west':
        if '1' in myPlayer.location:
            print("You have reached the end of the map. Don't go left.")
        else:
            destination = map.zonemap[myPlayer.location][LEFT]
            movement_handler(destination)
    elif dest == 'right' or dest == 'east':
        if '4' in myPlayer.location:
            print("You have reached the end of the map. Don't go right.")
        else:
            destination = map.zonemap[myPlayer.location][RIGHT]
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
    print(map.zonemap[myPlayer.location][EXAMINATION])

def player_talk():
    if myPlayer.xp != 0 and myPlayer.location == 'a1' or myPlayer.location == 'a4':
        dialogue = 'Thanks for getting rid of some monsters' + myPlayer.name + ', although there is still more'
    elif myPlayer.xp != 0 and myPlayer.location == 'b3':
        dialogue = 'I will give you 2 more levels if you kill more monsters for me.'
        myPlayer.xp = myPlayer.xp + 2000
    else:
        dialogue = map.zonemap[myPlayer.location][DIALOGUE]
    for character in dialogue:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)

def switch_weapon():
    askweaponsw = 'which weapon do you want to switch to?\n>'
    print('You can switch weapons now.')
    weapon_to_switch = input(askweaponsw)
    if weapon_to_switch == 'knife' and 'knife' in myPlayer.inventory:
        myPlayer.inventory.append(myPlayer.weapon)
        myPlayer.inventory.remove('knife')
        myPlayer.weapon = Knife()
        print('You equipped the ' + myPlayer.weapon.name)
    else:
        print('Are you sure you own that weapon?')

def stats():
    levels = str(math.floor((myPlayer.xp/1000)))
    print('#######################################################')
    print('                         STATS                         ')
    print('You are ' + myPlayer.name + ' the ' + myPlayer.job + '.')
    print('You have ' + str(myPlayer.hp) + ' hp.')
    print('You have ' + str(myPlayer.xp) + ' xp and you are at level ' + levels + '.')
    print('You have ' + str(myPlayer.ap) + ' strength.')
    print('Your current weapon, the ' + myPlayer.weapon.name + ' does ' + str(myPlayer.weapon.ap) + ' of damage.')
    print('Your Inventory contains ' + str(myPlayer.inventory) + ' .')
    print('#######################################################')


##### GAME FUNCTIONALITY #####
def start_game():
    setup_game()

def main_game_loop():
    print_location()
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
        myPlayer.ap = 40
        myPlayer.weapon = Sword()
    elif myPlayer.job == 'wizard':
        myPlayer.hp = 300
        myPlayer.ap = 20
        myPlayer.weapon = Staff()
    elif myPlayer.job == 'healer':
        myPlayer.hp = 200
        myPlayer.ap = 20
        myPlayer.heal = 40
        myPlayer.weapon = MagicBook()

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
    if myPlayer.location == 'b4':
        myPlayer.location = 'c1'
        map.zonemap[myPlayer.location][ZONENAME] = 'Telporter'
        destination = myPlayer.location
        movement_handler(destination)
    elif myPlayer.location == 'c1':
        myPlayer.location = 'b4'
        map.zonemap[myPlayer.location][ZONENAME] = 'Telporter'
        destination = myPlayer.location
        movement_handler(destination)
    elif myPlayer.location == 'd4':
        title_screen()
    elif myPlayer.location == 'b1':
        print('You pick up the knife')
        myPlayer.inventory.append('knife')
    elif myPlayer.location == 'b2':
        print1 = 'You take a nap'
        if myPlayer.job == 'fighter':
            myPlayer.hp = 120
        elif myPlayer.job == 'wizard':
            myPlayer.hp = 300
        elif myPlayer.job =='healer':
            myPlayer.hp = 200
        for character in print1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
    elif myPlayer.location == 'b3':
        print1 = 'You take a nap'
        if myPlayer.job == 'fighter':
            myPlayer.hp = 120
        elif myPlayer.job == 'wizard':
            myPlayer.hp = 300
        elif myPlayer.job =='healer':
            myPlayer.hp = 200
        for character in print1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
    elif myPlayer.location == 'c2':
        print1 = 'You take a nap'
        if myPlayer.job == 'fighter':
            myPlayer.hp = 120
        elif myPlayer.job == 'wizard':
            myPlayer.hp = 300
        elif myPlayer.job =='healer':
            myPlayer.hp = 200
        for character in print1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
    elif myPlayer.location == 'c3':
        print1 = 'You take a nap'
        if myPlayer.job == 'fighter':
            myPlayer.hp = 120
        elif myPlayer.job == 'wizard':
            myPlayer.hp = 300
        elif myPlayer.job =='healer':
            myPlayer.hp = 200
        for character in print1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
    elif myPlayer.location == 'c4':
        turn_based_combat()
    elif myPlayer.location == 'd3':
        thing = randint()
        combat(thing)
    elif myPlayer.location == 'd2':
        print('this beach is so sandy that...')
        print1 = 'you take a nap.'
        if myPlayer.job == 'fighter':
            myPlayer.hp = 120
        elif myPlayer.job == 'wizard':
            myPlayer.hp = 300
        elif myPlayer.job == 'healer':
            myPlayer.hp = 200
        for character in print1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(1)
    else:
        print(map.zonemap[myPlayer.location][ACTION])
    map.zonemap[myPlayer.location][SOLVED] = True

        if enemy == GreenS:
            print('##########################################')
            print('# A Green Slime appeared out of the dark #')
            print('##########################################')
        elif enemy == skeleton:
            print('#######################################')
            print('# A skeleton appeared out of the dark #')
            print('#######################################')
        elif enemy == zombie:
            print('#####################################')
            print('# A Zombie appeared out of the dark #')
            print('#####################################')
        while enemy.hp > 0:
            print('What would you like to do?')
            print("(You can type 'attack' to attack the monster.)")
            print("(If you are a healer, you can type 'heal' to heal.)")
            attack = input('> ')
            acceptable_attack = ['attack','kill', 'heal']
            while attack.lower().strip() not in acceptable_attack:
                print('Unknown action, try again.\n')
                attack = input('> ')
                if attack.lower().strip() == 'attack':
                    enemy.hp = enemy.hp - (myPlayer.weapon.ap + myPlayer.ap)
                    print("The monster's health is ")
                    print(enemy.hp)
                elif attack.lower().strip() == 'kill':
                    enemy.hp = 0
                    print("The monster's health is ")
                    print(enemy.hp)
            if attack.lower().strip() == 'attack':
                enemy.hp = enemy.hp - (myPlayer.ap + myPlayer.weapon.ap)
                if enemy.hp < 0:
                    enemy.hp = 0
                    print("The monster's health is ")
                    print(enemy.hp)
                else:
                    print("The monster's health is ")
                    print(enemy.hp)
            elif attack.lower().strip() == 'kill':
                enemy.hp = 0
                print("The monster's health is ")
                print(enemy.hp)
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
            if enemy.hp > 0:
                print('################################')
                print('# The Green Slime attacked you.#')
                print('################################')
                myPlayer.hp = myPlayer.hp - enemy.ap
                if myPlayer.hp <= 0:
                    myPlayer.hp = 0
                    myPlayer.game_over = True
                if myPlayer.game_over == True:
                    print('############################################')
                    print('# You are Dieing slowly, incased in slime. #')
                    print('############################################')
                    time.sleep(5)
                    title_screen()
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
        myPlayer.xp = myPlayer.xp + enemy.xp
        enemy.hp = 300
# def turn_based_combat():
#     random_attacker = (random.randint(1,3))
#     if random_attacker == 1 :
#         print('##########################################')
#         print('# A Green Slime appeared out of the dark #')
#         print('##########################################')
#         while enemy.hp > 0:
#             print('What would you like to do?')
#             print("(You can type 'attack' to attack the Green slime.)")
#             print("(If you are a healer, you can type 'heal' to heal.)")
#             attack = input('> ')
#             acceptable_attack = ['attack','kill', 'heal']
#             while attack.lower().strip() not in acceptable_attack:
#                 print('Unknown action, try again.\n')
#                 attack = input('> ')
#                 if attack.lower().strip() == 'attack':
#                     GreenS.hp = GreenS.hp - (myPlayer.weapon.ap + myPlayer.ap)
#                     print("The monster's health is ")
#                     print(GreenS.hp)
#                 elif attack.lower().strip() == 'kill':
#                     GreenS.hp = 0
#                     print("The monster's health is ")
#                     print(GreenS.hp)
#             if attack.lower().strip() == 'attack':
#                 GreenS.hp = GreenS.hp - (myPlayer.ap + myPlayer.weapon.ap)
#                 if GreenS.hp < 0:
#                     GreenS.hp = 0
#                     print("The monster's health is ")
#                     print(GreenS.hp)
#                 else:
#                     print("The monster's health is ")
#                     print(GreenS.hp)
#             elif attack.lower().strip() == 'kill':
#                 GreenS.hp = 0
#                 print("The monster's health is ")
#                 print(GreenS.hp)
#             if attack.lower().strip() == 'heal':
#                 if myPlayer.job == 'healer':
#                     myPlayer.hp = myPlayer.hp + myPlayer.heal
#                     if myPlayer.hp > 200:
#                         myPlayer.hp = 200
#                     text3 = 'You have '
#                     text4 = 'health now.\n'
#                     for character in text3:
#                         sys.stdout.write(character)
#                         sys.stdout.flush()
#                         time.sleep(0.1)
#                     print(myPlayer.hp)
#                     time.sleep(1)
#                     for character in text4:
#                         sys.stdout.write(character)
#                         sys.stdout.flush()
#                         time.sleep(0.1)
#                 else:
#                     print("You can't heal. You're not a healer.")
#             if GreenS.hp > 0:
#                 print('################################')
#                 print('# The Green Slime attacked you.#')
#                 print('################################')
#                 myPlayer.hp = myPlayer.hp - GreenS.ap
#                 if myPlayer.hp <= 0:
#                     myPlayer.hp = 0
#                     myPlayer.game_over = True
#                 if myPlayer.game_over == True:
#                     print('############################################')
#                     print('# You are Dieing slowly, incased in slime. #')
#                     print('############################################')
#                     time.sleep(5)
#                     title_screen()
#                 text = 'You have '
#                 text2 = 'health left.\n'
#                 for character in text:
#                     sys.stdout.write(character)
#                     sys.stdout.flush()
#                     time.sleep(0.1)
#                 print(myPlayer.hp)
#                 for character in text2:
#                     sys.stdout.write(character)
#                     sys.stdout.flush()
#                     time.sleep(0.1)
#         print('####################################')
#         print('# You have defeated a green slime. #')
#         print('#     You have gained 100 XP.      #')
#         print('####################################')
#         myPlayer.xp = myPlayer.xp + 100
#         GreenS.hp = 300
#     elif random_attacker == 2:
#         print('#######################################')
#         print('# A skeleton appeared out of the dark #')
#         print('#######################################')
#         while skeleton.hp > 0:
#             print('What would you like to do?')
#             print("(You can type 'attack' to attack the skeleton.)")
#             attack = input('> ')
#             acceptable_attack = ['attack','kill', 'heal']
#             while attack.lower().strip() not in acceptable_attack:
#                 print('Unknown action, try again.\n')
#                 attack = input('> ')
#                 if attack.lower().strip() == 'attack':
#                     skeleton.hp = skeleton.hp - (myPlayer.ap + myPlayer.weapon.ap)
#                     print("The skeleton's health is ")
#                     print(skeleton.hp)
#                 elif attack.lower().strip() == 'kill':
#                     skeleton.hp = 0
#                     print("The skeleton's health is ")
#                     print(skeleton.hp)
#             if attack.lower().strip() == 'attack':
#                 skeleton.hp = skeleton.hp - (myPlayer.ap + myPlayer.weapon.ap)
#                 if skeleton.hp < 0:
#                     skeleton.hp = 0
#                     print("The skeleton's health is ")
#                     print(skeleton.hp)
#                 else:
#                     print("The skeleton's health is ")
#                     print(skeleton.hp)
#             elif attack.lower().strip() == 'kill':
#                 skeleton.hp = 0
#                 print("The skeleton's health is ")
#                 print(skeleton.hp)
#             if attack.lower().strip() == 'heal':
#                 if myPlayer.job == 'healer':
#                     myPlayer.hp = myPlayer.hp + myPlayer.heal
#                     if myPlayer.hp > 200:
#                         myPlayer.hp = 200
#                     text3 = 'You have '
#                     text4 = 'health now.\n'
#                     for character in text3:
#                         sys.stdout.write(character)
#                         sys.stdout.flush()
#                         time.sleep(0.1)
#                     print(myPlayer.hp)
#                     time.sleep(1)
#                     for character in text4:
#                         sys.stdout.write(character)
#                         sys.stdout.flush()
#                         time.sleep(0.1)
#                 else:
#                     print("You can't heal. You're not a healer.")
#             if skeleton.hp > 0:
#                 print('\n##########################')
#                 print('# The skeleton attacked you. #')
#                 print('############################')
#                 myPlayer.hp = myPlayer.hp - skeleton.ap
#                 if myPlayer.hp <= 0:
#                     myPlayer.hp = 0
#                     myPlayer.game_over = True
#                 if myPlayer.game_over == True:
#                     print('#####################################################')
#                     print('# You are Dead, with a arrow inpaled in your heart. #')
#                     print('#####################################################')
#                     time.sleep(5)
#                     title_screen()
#                 text = 'You have '
#                 text2 = 'health left.\n'
#                 for character in text:
#                     sys.stdout.write(character)
#                     sys.stdout.flush()
#                     time.sleep(0.1)
#                 print(myPlayer.hp)
#                 for character in text2:
#                     sys.stdout.write(character)
#                     sys.stdout.flush()
#                     time.sleep(0.1)
#         print('####################################')
#         print('#   You have defeated a skeleton.  #')
#         print('#     You have gained 300 XP.      #')
#         print('####################################')
#         myPlayer.xp = myPlayer.xp + 300
#         skeleton.hp = 500
#     elif random_attacker == 3:
#         print('#####################################')
#         print('# A Zombie appeared out of the dark #')
#         print('#####################################')
#         while zombie.hp > 0:
#             print('What would you like to do?')
#             print("(You can type 'attack' to attack the Zombie.)")
#             attack = input('> ')
#             acceptable_attack = ['attack','kill', 'heal']
#             while attack.lower().strip() not in acceptable_attack:
#                 print('Unknown action, try again.\n')
#                 attack = input('> ')
#                 if attack.lower().strip() == 'attack':
#                     zombie.hp = zombie.hp - (myPlayer.ap + myPlayer.weapon.ap)
#                     print("The Zombie's health is ")
#                     print(zombie.hp)
#                 elif attack.lower().strip() == 'kill':
#                     zombie.hp = 0
#                     print("The Zombie's health is ")
#                     print(zombie.hp)
#             if attack.lower().strip() == 'attack':
#                 zombie.hp = zombie.hp - (myPlayer.ap + myPlayer.weapon.ap)
#                 if zombie.hp < 0:
#                     zombie.hp = 0
#                     print("The Zombie's health is ")
#                     print(zombie.hp)
#                 else:
#                     print("The Zombie's health is ")
#                     print(zombie.hp)
#             elif attack.lower().strip() == 'kill':
#                 zombie.hp = 0
#                 print("The Zombie's health is ")
#                 print(zombie.hp)
#             if attack.lower().strip() == 'heal':
#                 if myPlayer.job == 'healer':
#                     myPlayer.hp = myPlayer.hp + myPlayer.heal
#                     if myPlayer.hp > 200:
#                         myPlayer.hp = 200
#                     text3 = 'You have '
#                     text4 = 'health now.\n'
#                     for character in text3:
#                         sys.stdout.write(character)
#                         sys.stdout.flush()
#                         time.sleep(0.1)
#                     print(myPlayer.hp)
#                     time.sleep(1)
#                     for character in text4:
#                         sys.stdout.write(character)
#                         sys.stdout.flush()
#                         time.sleep(0.1)
#                 else:
#                     print("You can't heal. You're not a healer.")
#             if zombie.hp > 0:
#                 print('\n##########################')
#                 print('# The Zombie attacked you. #')
#                 print('############################')
#                 myPlayer.hp = myPlayer.hp - zombie.ap
#                 if myPlayer.hp <= 0:
#                     myPlayer.hp = 0
#                     myPlayer.game_over = True
#                 if myPlayer.game_over == True:
#                     print('##########################################################################')
#                     print('# You are now a zombie as the zombie who just killed you is now a human. #')
#                     print('##########################################################################')
#                     time.sleep(5)
#                     title_screen()
#                 text = 'You have '
#                 text2 = 'health left.\n'
#                 for character in text:
#                     sys.stdout.write(character)
#                     sys.stdout.flush()
#                     time.sleep(0.1)
#                 print(myPlayer.hp)
#                 for character in text2:
#                     sys.stdout.write(character)
#                     sys.stdout.flush()
#                     time.sleep(0.1)
#         print('####################################')
#         print('#   You have defeated a zombie.    #')
#         print('#     You have gained 500 XP.      #')
#         print('####################################')
#         myPlayer.xp = myPlayer.xp + 500
#         zombie.hp = 500
#     map.zonemap[myPlayer.location][SOLVED] = True
#     main_game_loop()

print('________________        _________            _______ ______          _______ _      _________        _______ _______             _______ _______ _______ _______  ')
print('\__   __(  ____ |\     /\__   __/           (  ___  (  __  \|\     /(  ____ ( (    /\__   __|\     /(  ____ (  ____ \           (  ____ (  ___  (       (  ____ \ ')
print('   ) (  | (    \( \   / )  ) (              | (   ) | (  \  | )   ( | (    \|  \  ( |  ) (  | )   ( | (    )| (    \/           | (    \| (   ) | () () | (    \/ ')
print('   | |  | (__    \ (_) /   | |      _____   | (___) | |   ) | |   | | (__   |   \ | |  | |  | |   | | (____)| (__       _____   | |     | (___) | || || | (__     ')
print('   | |  |  __)    ) _ (    | |     (_____)  |  ___  | |   | ( (   ) |  __)  | (\ \) |  | |  | |   | |     __|  __)     (_____)  | | ____|  ___  | |(_)| |  __)    ')
print('   | |  | (      / ( ) \   | |              | (   ) | |   ) |\ \_/ /| (     | | \   |  | |  | |   | | (\ (  | (                 | | \_  | (   ) | |   | | (       ')
print('   | |  | (____/( /   \ )  | |              | )   ( | (__/  ) \   / | (____/| )  \  |  | |  | (___) | ) \ \_| (____/\           | (___) | )   ( | )   ( | (____/\ ')
print('   )_(  (_______|/     \|  )_(              |/     \(______/   \_/  (_______|/    )_)  )_(  (_______|/   \__(_______/           (_______|/     \|/     \(_______/ ')

title_screen()
