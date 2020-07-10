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
screen_width = 1000

godbool = '1'
##### Player Setup #####
class Player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.max = 0
        self.ap = 0
        self.heal = 0
        self.status_effects = []
        self.armour = []
        self.shield = False
        self.location = 'b2'
        self.game_over = False
        self.inventory = []
        self.weapon = ''
        self.xp = 0
        self.money = 0
myPlayer = Player()

class Gslime:
    def __init__(self):
        self.hp = 300
        self.ap = 20
        self.xp = 100
        self.money = 10
        self.max = 300
        self.appear = '##########################################\n# A Green Slime appeared out of the dark #\n##########################################'
        self.attack = '################################\n# The Green Slime attacked you.#\n################################'
        self.die = '############################################\n# You are Dieing slowly, incased in slime. #\n############################################'
        self.defeat = '####################################\n# You have defeated a green slime. #\n#     You have gained 100 XP.      #\n#    You have gained 10 money.     #\n####################################\n'
GreenS = Gslime()
class Zomboy:
    def __init__(self):
        self.hp = 500
        self.ap = 40
        self.xp = 500
        self.money = 25
        self.max = 500
        self.appear = '#####################################\n# A Zombie appeared out of the dark #\n#####################################'
        self.attack = '############################\n# The Zombie attacked you. #\n############################'
        self.die = '##########################################################################\n# You are now a zombie as the zombie who just killed you is now a human. #\n##########################################################################'
        self.defeat = '####################################\n#   You have defeated a zombie.    #\n#     You have gained 500 XP.      #\n#    You have gained 25 money.     #\n####################################\n'
zombie = Zomboy()
class Skelemob:
    def __init__(self):
        self.hp = 500
        self.ap = 40
        self.xp = 500
        self.money = 25    
        self.max = 500
        self.appear = '#######################################\n# A skeleton appeared out of the dark #\n#######################################'
        self.attack = '##############################\n# The skeleton attacked you. #\n##############################'
        self.die = '#####################################################\n# You are Dead, with a arrow inpaled in your heart. #\n#####################################################'
        self.defeat = '####################################\n#   You have defeated a skeleton.  #\n#    You have gained 25 money.     #\n#     You have gained 300 XP.      #\n####################################\n'
skeleton = Skelemob()
class Sword:
    def __init__(self):
        self.nick = 'sword'
        self.name = "Soldier's Broadsword"
        self.ap = 100
class Staff:
    def __init__(self):
        self.nick = 'staff'
        self.name = "Wizard's Arcane Staff"
        self.ap = 75
class MagicBook:
    def __init__(self):
        self.nick = 'book'
        self.name = "Healer's Book of Magic"
        self.ap = 50
class Knife:
    def __init__(self):
        self.nick = 'knife'
        self.name = "Traveller's Knife"
        self.ap = 80
class Boots:
    def __init__(self):
        self.nick = 'boots'
        self.name = 'Iron Boots'
        self.hp = 30
        self.durability = 100
class Leggings:
    def __init__(self):
        self.nick = 'leggings'
        self.name = 'Iron Leggings'
        self.hp = 40
        self.durability = 100
class Chestplate:
    def __init__(self):
        self.nick = 'chestplate'
        self.name = 'Iron Chestplate'
        self.hp = 60
        self.durability = 100
class Helmet:
    def __init__(self):
        self.nick = 'helmet'
        self.name = 'Iron Helmet'
        self.hp = 50
        self.durability = 100
class Shield:
    def __init__(self):
        self.nick = 'shield'
        self.name = myPlayer.job + "'s Shield"

##### name to weapon linking ####
weapon_to_class = {
    'knife' : Knife(),
    'sword' : Sword(),
    'staff' : Staff(),
    'book' : MagicBook(),
}
armour_to_class = {
    'helmet' : Helmet(),
    'chestplate' : Chestplate(),
    'leggings' : Leggings(),
    'boots' : Boots(),
}

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
    print('# • Go to the store to buy    #')
    print('#  armour                     #')
    print('# • Equip your armour for     #')
    print('#  extra health.              #')
    print('#   Copyright 2019 tejmen09   #')
    print('###############################')
    title_screen()
def acknowledgements_menu():
    print('###############################')
    print('#       Acknowledgements      #')
    print('# Beta Tested By:             #')
    print('# • Manas Mengle              #')
    print('# • Pranot Mengle             #')
    print('# • Meenakshi Mengle          #')
    print('# Helped By:                  #')
    print('# • Manas Mengle              #')
    print('# • Pranot Mengle             #')
    print('# Copyright 2019 Tejas Mengle #')
    print('###############################')
    time.sleep(3)
    title_screen()



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
    print("(You can 'move', 'quit', 'look', 'talk', 'equip', 'help', 'stats' or 'act')")
    action = input('> ')
    acceptable_actions = ['move', 'quit', 'look', '/god', 'acceptable_actions', 'act', 'talk', 'equip', 'stats', 'money', 'help']
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
    elif action.lower().strip() == 'equip':
        switch_weapon()
    elif action.lower().strip() == 'stats':
        stats()
    elif action.lower().strip() == 'help':
        help_menu()
    elif action.lower().strip() == 'money':
        myPlayer.money = input('Money = ?\n')

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
    else:
        dialogue = map.zonemap[myPlayer.location][DIALOGUE]
    for character in dialogue:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)

def switch_weapon():
    askweaponsw = 'which weapon do you want to switch to?\n>'
    print('You can switch weapons now.')
    equipment_to_switch = input(askweaponsw)
    if equipment_to_switch in weapon_to_class and equipment_to_switch in myPlayer.inventory:
        myPlayer.inventory.append(myPlayer.weapon.nick)
        myPlayer.inventory.remove(equipment_to_switch)
        myPlayer.weapon = weapon_to_class[equipment_to_switch]
        print('You equipped the ' + myPlayer.weapon.name)
    elif equipment_to_switch in armour_to_class and equipment_to_switch in myPlayer.inventory:
        myPlayer.inventory.remove(equipment_to_switch)
        myPlayer.armour.append(armour_to_class[equipment_to_switch])
        print('You equipped the ' + equipment_to_switch)
    elif equipment_to_switch and equipment_to_switch in myPlayer.inventory:
        myPlayer.shield = True
        myPlayer.inventory.remove(equipment_to_switch)
    else:
        print('Are you sure you own that weapon?')

def stats():
    levels = math.floor((myPlayer.xp/1000))
    print('#######################################################')
    print('#                         STATS                         ')
    print('# You are ' + myPlayer.name + ' the ' + myPlayer.job + '.')
    print('# You have ' + str(myPlayer.hp) + ' hp.')
    print('# You have ' + str(myPlayer.xp) + ' xp and you are at level ' + str(levels) + '.')
    print('# You have ' + str(myPlayer.ap) + ' strength.')
    print('# You have ₴ ' + str(myPlayer.money))
    print('# Your current weapon, the ' + myPlayer.weapon.name + ' does ' + str(myPlayer.weapon.ap) + ' of damage.')
    print('# Your Inventory contains: ', end='')
    for a in myPlayer.inventory:
        print(a + ',', end='')
    print('.')
    print('# You are wearing these pieces of armour: ', end='')
    for a in myPlayer.armour:
        print(a.name + ',', end='')
    print('.')
    print('#######################################################')

def shop():
    print('#######################################################################################################')
    print('#                                          SHOP              #                                        #')
    print('#                            #        ████████████████       #       ██████████████████████████       #')
    print('#      ██████    ██████      #      ██              ▒▒██     #     ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██     #')
    print('#    ██  ▒▒██    ██  ▒▒██    #      ██              ▒▒██     #     ██▒▒                      ▒▒██     #')
    print('#    ██  ▒▒██    ██  ▒▒██    #      ██    ▒▒▒▒▒▒▒▒  ▒▒██     #     ██▒▒                      ▒▒██     #')
    print('#    ██  ▒▒██    ██  ▒▒██    #      ██  ▒▒▒▒████▒▒  ▒▒██     #     ██▒▒                      ▒▒██     #')
    print("#  ██    ▒▒██    ██      ██  #      ██  ▒▒██    ██  ▒▒██     #     ██▒▒                      ▒▒██     #")
    print('#██    ▒▒▒▒██    ██▒▒    ▒▒██#      ██  ▒▒██    ██  ▒▒██     #     ██▒▒                      ▒▒██     #')
    print('#██▒▒▒▒▒▒██        ██▒▒▒▒▒▒██#      ██  ▒▒██    ██  ▒▒██     #     ██▒▒                      ▒▒██     #')
    print('#████████            ████████#      ██▒▒▒▒██    ██▒▒▒▒██     #     ██▒▒                      ▒▒██     #')
    print('#                            #      ████████    ████████     #     ██▒▒          ██          ▒▒██     #')
    print('#   [1]Boots        ₴ 10     #  [2]Leggings     ₴ 20         #     ██▒▒        ██████        ▒▒██     #')
    print('##############################################################     ██▒▒          ██          ▒▒██     #')
    print('#                            #       ████        ████        #     ██▒▒                      ▒▒██     #')
    print('#                            #   ████  ▒▒██    ██    ████    #     ██▒▒                      ▒▒██     #')
    print('#       ████████████         # ██      ▒▒██    ██      ▒▒██  #     ██▒▒                      ▒▒██     #')
    print('#     ██          ▒▒██       # ██          ████        ▒▒██  #     ██▒▒                      ▒▒██     #')
    print('#   ██            ▒▒▒▒██     # ██▒▒                  ▒▒▒▒██  #     ██▒▒                      ▒▒██     #')
    print('#   ██          ▒▒▒▒▒▒██     #   ██                ▒▒▒▒██    #       ██▒▒                  ▒▒██       #')
    print('#   ██    ████████▒▒▒▒██     #   ██▒▒              ▒▒▒▒██    #         ██▒▒              ▒▒██         #')
    print('#   ██  ████████████▒▒██     #     ██              ▒▒██      #           ██▒▒          ▒▒██           #')
    print('#   ██  ████████████▒▒██     #     ██            ▒▒▒▒██      #             ██▒▒▒▒▒▒▒▒▒▒██             #')
    print('#     ████        ████       #     ██▒▒        ▒▒▒▒▒▒██      #               ██▒▒▒▒▒▒██               #')
    print('#                            #     ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██      #                 ██▒▒██                 #')
    print('#                            #       ██▒▒▒▒▒▒▒▒▒▒▒▒██        #                   ██                   #')
    print('#                            #         ████████████          #                                        #')
    print('#                            #                               #                                        #')
    print('#    [3]Helmet      ₴ 30     #      [4]Chestplate ₴ 40       #     [5]Shield     ₴ 35                 #')
    print('#######################################################################################################')
    print('#         TYPE THE THING YOU WANT TO BUY TO PURCHASE!        #')
    print('#                  TYPE BACK TO GO BACK!                     #')
    cart = input('> ')
    acceptable_cart = ['1','2', '3', '4', '5','back']
    while cart.lower().strip() not in acceptable_cart:
        print('Unknown action, try again.\n')
        cart = input('> ')
    if cart.lower().strip() == '1':
        #PURCHASE BOOTS
        myPlayer.inventory.append('boots')
        print('You have purchased the Iron Boots.')
    if cart.lower().strip() == '2':
        #PURCHASE LEGGINGS
        myPlayer.inventory.append('leggings')
        print('You have purchased the Iron Leggings.')
    if cart.lower().strip() == '3':
        #PURCHASE HELMET
        myPlayer.inventory.append('helmet')
        print('You have purchased the Iron Helmet.')
    if cart.lower().strip() == '4':
        #PURCHASE CHESTPLATE
        myPlayer.inventory.append('chestplate')
        print('You have purchased the Iron Chestplate.')
    if cart.lower().strip() == '5':
        #PURCAHSE SHIELD
        myPlayer.inventory.append('shield')
        print('You have purchased the shield.') 
    if cart.lower().strip() == 'back':
        main_game_loop()
       


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
        myPlayer.max = 120
        myPlayer.hp = myPlayer.max
        myPlayer.ap = 40
        myPlayer.weapon = Sword()
    elif myPlayer.job == 'wizard':
        myPlayer.max = 300
        myPlayer.hp = myPlayer.max
        myPlayer.ap = 20
        myPlayer.weapon = Staff()
    elif myPlayer.job == 'healer':
        myPlayer.max = 200
        myPlayer.hp = myPlayer.max
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
    if map.zonemap[myPlayer.location][SOLVED] == False:
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
            myPlayer.hp = myPlayer.max
            for character in print1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(1)
        elif myPlayer.location == 'b3':
            if not myPlayer.money == 0:
                print1 = '"I will give you some money if you defeat the monsters south of here" said an old man.'
            else:
                print1 = 'I have given you some money.\n Now go away!'
                for character in print1:
                    sys.stdout(character)
                    sys.stdout.flush()
                    time.sleep(0.1)
                myPlayer.money = myPlayer.money + 40
                map.zonemap[myPlayer.location][SOLVED] = True
            time.sleep(1)
        elif myPlayer.location == 'c2':
            print1 = 'You take a nap'
            myPlayer.hp = myPlayer.max
            for character in print1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(1)
        elif myPlayer.location == 'c3':
            print1 = 'You take a nap'
            myPlayer.hp = myPlayer.max
            for character in print1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(1)
        elif myPlayer.location == 'c4':
            turn_based_combat()
        elif myPlayer.location == 'd3':
            turn_based_combat()
        elif myPlayer.location == 'd2':
            print('this beach is so sandy that...')
            print1 = 'you take a nap.'
            myPlayer.hp = myPlayer.max
            for character in print1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(1)
        elif myPlayer.location == 'a1':
            if myPlayer.money == 0:
                print1 = '"Go get money so you can buy stuff!" shouts one of the merchants'
                for character in print1:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                time.sleep(0.1)
            else:
                shop()
        else:
            print(map.zonemap[myPlayer.location][ACTION])
    else:
        print('There is nothing to do here!')
        

def combat(enemy, name):
    print(enemy.appear)
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
            print(enemy.attack)
            myPlayer.hp = myPlayer.hp - enemy.ap
            if myPlayer.hp <= 0:
                myPlayer.hp = 0
                myPlayer.game_over = True
            if myPlayer.game_over == True:
                print(enemy.die)
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
    print(enemy.defeat)
    myPlayer.xp = myPlayer.xp + enemy.xp
    myPlayer.money = myPlayer.money + enemy.money
    levels = math.floor((myPlayer.xp/1000))
    if levels%10 == 0:
        myPlayer.ap = myPlayer.ap + 1
    enemy.hp = enemy.max
def turn_based_combat():
    random_attacker = (random.randint(1,3))
    if random_attacker == 1 :
        combat(GreenS, 'slime')
    elif random_attacker == 2:
        combat(skeleton, 'skeleton')
    elif random_attacker == 3:
        combat(zombie, 'zombie')
    main_game_loop()

print('________________        _________            _______ ______          _______ _      _________        _______ _______             _______ _______ _______ _______  ')
print('\__   __(  ____ |\     /\__   __/           (  ___  (  __  \|\     /(  ____ ( (    /\__   __|\     /(  ____ (  ____ \           (  ____ (  ___  (       (  ____ \ ')
print('   ) (  | (    \( \   / )  ) (              | (   ) | (  \  | )   ( | (    \|  \  ( |  ) (  | )   ( | (    )| (    \/           | (    \| (   ) | () () | (    \/ ')
print('   | |  | (__    \ (_) /   | |      _____   | (___) | |   ) | |   | | (__   |   \ | |  | |  | |   | | (____)| (__       _____   | |     | (___) | || || | (__     ')
print('   | |  |  __)    ) _ (    | |     (_____)  |  ___  | |   | ( (   ) |  __)  | (\ \) |  | |  | |   | |     __|  __)     (_____)  | | ____|  ___  | |(_)| |  __)    ')
print('   | |  | (      / ( ) \   | |              | (   ) | |   ) |\ \_/ /| (     | | \   |  | |  | |   | | (\ (  | (                 | | \_  | (   ) | |   | | (       ')
print('   | |  | (____/( /   \ )  | |              | )   ( | (__/  ) \   / | (____/| )  \  |  | |  | (___) | ) \ \_| (____/\           | (___) | )   ( | )   ( | (____/\ ')
print('   )_(  (_______|/     \|  )_(              |/     \(______/   \_/  (_______|/    )_)  )_(  (_______|/   \__(_______/           (_______|/     \|/     \(_______/ ')

title_screen()
