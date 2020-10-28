# Python Text RPG
# Created by tej_men
#     \
# (:D)-<
#     /


import math
import random
import sys
import time
import map

screen_width = 1000

godbool = '1'


def reset():
    myPlayer.name = ''
    myPlayer.name = ''
    myPlayer.job = ''
    myPlayer.job = ''
    myPlayer.hp = 0
    myPlayer.max = 0
    myPlayer.ap = 0
    myPlayer.heal = 0
    myPlayer.status_effects = []
    myPlayer.armour = []
    myPlayer.shield = False
    myPlayer.location = 'b2'
    myPlayer.game_over = False
    myPlayer.inventory = []
    myPlayer.weapon = ''
    myPlayer.xp = 0
    myPlayer.money = 0
    myPlayer.missions = []


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
        self.missions = []


myPlayer = Player()


class Gslime:
    def __init__(self):
        self.hp = 300
        self.ap = 40
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
        self.ap = 60
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
        self.ap = 60
        self.xp = 500
        self.money = 25
        self.max = 500
        self.appear = '#######################################\n# A skeleton appeared out of the dark #\n#######################################'
        self.attack = '##############################\n# The skeleton attacked you. #\n##############################'
        self.die = '#####################################################\n# You are Dead, with a arrow impaled in your heart. #\n#####################################################'
        self.defeat = '####################################\n#   You have defeated a skeleton.  #\n#    You have gained 25 money.     #\n#     You have gained 300 XP.      #\n####################################\n'


skeleton = Skelemob()

class Spideeer:
    def __init__(self):
        self.hp = 600
        self.ap = 10
        self.status_effects = 'poison'
        self.xp = 500
        self.money = 25
        self.max = 500
        self.appear = '#######################################\n# A spider appeared out of the dark #\n#######################################'
        self.attack = '##############################\n# The spider attacked you. #\n##############################'
        self.die = '#####################################################\n# You are Dead, biten by the spider. #\n#####################################################'
        self.defeat = '####################################\n#   You have defeated a spider.    #\n#    You have gained 40 money.     #\n#     You have gained 500 XP.      #\n####################################\n'
spider = Spideeer()
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
        self.dp = 5
        self.durability = 100


class Leggings:
    def __init__(self):
        self.nick = 'leggings'
        self.name = 'Iron Leggings'
        self.dp = 15
        self.durability = 100


class Chestplate:
    def __init__(self):
        self.nick = 'chestplate'
        self.name = 'Iron Chestplate'
        self.dp = 20
        self.durability = 100


class Helmet:
    def __init__(self):
        self.nick = 'helmet'
        self.name = 'Iron Helmet'
        self.dp = 10
        self.durability = 100


class Shield:
    def __init__(self):
        self.nick = 'shield'
        self.name = myPlayer.job + "'s Shield"


##### name to weapon linking ####
weapon_to_class = {
    'knife': Knife(),
    'sword': Sword(),
    'staff': Staff(),
    'book': MagicBook(),
}
armour_to_class = {
    'helmet': Helmet(),
    'chestplate': Chestplate(),
    'leggings': Leggings(),
    'boots': Boots(),
}


##### Title Screen #####
def title_screen_selections():
    option = input("> ")
    if option.lower().strip() == "play":
        start_game()  # placeholder until written
    elif option.lower().strip() == "help":
        help_menu(False)
    elif option.lower().strip() == "quit":
        print('You have')
        print(myPlayer.xp)
        print('xp.')
        print('###############')
        print('#  GOODBYE!!  #')
        print('###############')
        time.sleep(0.5)
        sys.exit()
    elif option.lower().strip() == 'resume':
        main_game_loop()
    elif option.lower().strip() == "acknowledgements":
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
        if option.lower().strip() == "play":
            start_game()
        elif option.lower().strip() == "help":
            help_menu(False)
        elif option.lower().strip() == "quit":
            print('You have')
            print(myPlayer.xp)
            print('xp.')
            print('###############')
            print('#  GOODBYE!!  #')
            print('###############')
            time.sleep(0.5)
            sys.exit()
        elif option.lower().strip() == 'resume':
            main_game_loop()
        elif option.lower().strip() == "acknowledgements":
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


def help_menu(ingame):
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
    if ingame:
        main_game_loop()
    elif not ingame:
        title_screen()


def acknowledgements_menu():
    print('###############################')
    print('#       Acknowledgements      #')
    print('# Beta Tested By:             #')
    print('# • Manas Mengle              #')
    print('# • Pranot Mengle             #')
    print('# • Meenakshi Mengle          #')
    print('# • Anahita Maradani          #')
    print('# Helped By:                  #')
    print('# • Manas Mengle              #')
    print('# • Pranot Mengle             #')
    print('# Copyright 2019 Tejas Mengle #')
    print('###############################')
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
    print('# ' + map.zonemap[myPlayer.location][ZONENAME] + ' ' * (
            len(map.zonemap[myPlayer.location][DESCRIPTION]) - len(
        map.zonemap[myPlayer.location][ZONENAME])) + ' #')
    print('# ' + map.zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print('#' * (4 + len(map.zonemap[myPlayer.location][DESCRIPTION])))


def prompt():
    print('\n' + '===============================')
    print('What would you like to do?')
    print("(You can 'move', 'quit', 'look', 'talk', 'equip', 'help', 'stats' or 'act' or 'mission')")
    action = input('> ')
    acceptable_actions = ['move', 'quit', 'look', 'act', 'talk', 'equip', 'stats', 'money', 'help','mission']
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
    elif action.lower().strip() == 'look':
        player_examine()
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
        help_menu(True)
    elif action.lower().strip() == 'mission':
        mission()
    elif action.lower().strip() == 'money':
        myPlayer.money = int(input('Money = ?\n'))


def player_move():
    ask = 'Where would you like to move to?\n'
    print("You can move 'up', 'down', 'left' or 'right'.")
    dest = input(ask)
    if dest == 'up' and map.zonemap[myPlayer.location][UP] != 'null':
        print(map.zonemap[myPlayer.location][UP])
        destination = map.zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest == 'down' and map.zonemap[myPlayer.location][DOWN] != 'null':
        print(map.zonemap[myPlayer.location][DOWN])
        destination = map.zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest == 'left' and map.zonemap[myPlayer.location][LEFT] != 'null':
        print(map.zonemap[myPlayer.location][LEFT])
        destination = map.zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest == 'right' and map.zonemap[myPlayer.location][RIGHT] != 'null':
        print(map.zonemap[myPlayer.location][RIGHT])
        destination = map.zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest == 'tp':
        print('Where do you want to go god?')
        qa = input('_')
        myPlayer.location = qa
        destination = myPlayer.location
        movement_handler(destination)
    else:
        print("You have reached the end of the map.")


def movement_handler(destination):
    print('\n' + 'You have moved to ' + destination + '.')
    myPlayer.location = destination
    print_location()


def player_examine():
    print(map.zonemap[myPlayer.location][EXAMINATION])


def player_talk():
    if myPlayer.xp != 0 and myPlayer.location == 'a1' or myPlayer.location == 'a4':
        dialogue = 'Thanks for getting rid of some monsters' + myPlayer.name + ', although there is still more'
    elif myPlayer.location == 'f1':
        dialogue = "'You want to open the chest! \n I locked it away when the creaures came. 'said the farm owner\n Here you go"
        myPlayer.inventory.append('key')
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
    elif equipment_to_switch == 'shield' and equipment_to_switch in myPlayer.inventory:
        myPlayer.shield = True
        myPlayer.inventory.remove(equipment_to_switch)
        print('You have equipped the ' + myPlayer.job + "'s Shield")
    else:
        print('Are you sure you own that weapon?')


def stats():
    levels = math.floor((myPlayer.xp / 1000))
    print('#######################################################')
    print('#                         STATS                        ')
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
    print('                                    TYPE THE THING YOU WANT TO BUY TO PURCHASE!                        ')
    print('                                               TYPE BACK TO GO BACK!                                   ')
    print('                                    YOU HAVE ₴ ' + str(myPlayer.money) + '.                    ')
    cart = input('> ')
    acceptable_cart = ['1', '2', '3', '4', '5', 'back']
    while cart.lower().strip() not in acceptable_cart:
        print('Unknown action, try again.\n')
        cart = input('> ')
    if cart.lower().strip() == '1':
        # PURCHASE BOOTS
        if myPlayer.money > 9:
            myPlayer.inventory.append('boots')
            myPlayer.money -= 10
            print('You have purchased the Iron Boots.')
        else:
            print('You do not have enough money!')
    if cart.lower().strip() == '2':
        # PURCHASE LEGGINGS
        if myPlayer.money > 19:
            myPlayer.inventory.append('leggings')
            myPlayer.money -= 20
            print('You have purchased the Iron Leggings.')
        else:
            print('You do not have enough money!')
    if cart.lower().strip() == '3':
        # PURCHASE HELMET
        if myPlayer.money > 29:
            myPlayer.inventory.append('helmet')
            myPlayer.money -= 30
            print('You have purchased the Iron Helmet.')
        else:
            print('You do not have enough money!')
    if cart.lower().strip() == '4':
        # PURCHASE CHESTPLATE
        if myPlayer.money > 39:
            myPlayer.inventory.append('chestplate')
            myPlayer.money -= 40
            print('You have purchased the Iron Chestplate.')
        else:
            print('You do not have enough money!')
    if cart.lower().strip() == '5':
        # PURCHASE SHIELD
        if myPlayer.money > 34:
            myPlayer.inventory.append('shield')
            myPlayer.money -= 35
            print('You have purchased the shield.')
        else:
            print('You do not have enough money!')

    if cart.lower().strip() == 'back':
        main_game_loop()

def mission():
    comma_needed = ''
    if len(myPlayer.missions) > 1:
        comma_needed = ','
    print('#########################################')
    print('#               Missions                #')
    print('# • ', end='' )
    for a in myPlayer.missions:
        print(a + comma_needed, end='')
    if len(myPlayer.missions) != 1:
        comma_needed = ','
    print('.')
    print('#########################################')

##### GAME FUNCTIONALITY #####
def start_game():
    setup_game()


def main_game_loop():
    print_location()
    while myPlayer.game_over is False:
        prompt()


def setup_game():
    reset()
    ### NAME COLLECTING ###
    question1 = 'What is your name young traveller?\n'
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    if player_name == 'dev':
        myPlayer.name = 'Developer'
        myPlayer.job = 'fighter'
        myPlayer.max = 120
        myPlayer.hp = myPlayer.max
        myPlayer.ap = 40
        myPlayer.weapon = Sword()
        myPlayer.inventory = ['shield']
        main_game_loop()
    else:
        myPlayer.name = player_name
    ### JOB HANDELLING ###
    question2 = 'What is will your role be ' + player_name + '?\n'
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
    question3 = 'Welcome ' + player_name + ' the ' + player_job + '.\n'
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
    if not map.zonemap[myPlayer.location][SOLVED]:
        exec(map.zonemap[myPlayer.location][ACTION])
    else:
        print('There is nothing to do here!')


def combat(enemy):
    willdefend = False
    print(enemy.appear)
    while enemy.hp > 0:
        print('What would you like to do?')
        print("(You can type 'attack' to attack the monster.)")
        print("(If you are a healer, you can type 'heal' to heal.)")
        if 'shield' in myPlayer.inventory:
            print("(You own a shield! type 'defend' to (hopefully) protect you from the enemy's attack!")
        attack = input('> ')
        acceptable_attack = ['attack', 'kill', 'heal', 'defend']
        while attack.lower().strip() not in acceptable_attack:
            print('Unknown action, try again.\n')
            attack = input('> ')
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
        elif attack.lower().strip() == 'heal':
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
        elif attack.lower().strip() == 'defend':
            if 'shield' in myPlayer.inventory:
                defends = random.randint(0, 10)
                if defends < 7:
                    willdefend = True
                    print("Your defence was successful, and the shield deflected the blow")
                else:
                    willdefend = False
                    print("Unfortunately, your defence failed.")
                    print(enemy.attack)
        if enemy.hp > 0:
            damage = enemy.ap
            for i in myPlayer.armour:
                damage = damage - math.floor((i.dp / 2))
                i.durability -= 1
            if not willdefend:
                myPlayer.hp -= damage
            if myPlayer.hp <= 0:
                myPlayer.hp = 0
                myPlayer.game_over = True
                main_game_loop()
            if myPlayer.game_over:
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
    myPlayer.xp += enemy.xp
    myPlayer.money += enemy.money
    levels = math.floor((myPlayer.xp / 1000))
    if levels % 10 == 0:
        myPlayer.ap = myPlayer.ap + 1
    enemy.hp = enemy.max


def turn_based_combat():
    enemies = [GreenS, skeleton, zombie]
    random_attacker = (random.choice(enemies))
    combat(random_attacker)
    main_game_loop()


def new_map():
    sequence = 'You look through the portal, deciding whether or not to go to wherever the portal goes\nUnsure,you step into the portal going wherever the portal takes you.'
    for character in sequence:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    

print('________________        _________            _______ ______          _______ _      _________        _______ _______             _______ _______ _______ _______  ')
print('\__   __(  ____ |\     /\__   __/           (  ___  (  __  \|\     /(  ____ ( (    /\__   __|\     /(  ____ (  ____ \           (  ____ (  ___  (       (  ____ \ ')
print('   ) (  | (    \( \   / )  ) (              | (   ) | (  \  | )   ( | (    \|  \  ( |  ) (  | )   ( | (    )| (    \/           | (    \| (   ) | () () | (    \/ ')
print('   | |  | (__    \ (_) /   | |      _____   | (___) | |   ) | |   | | (__   |   \ | |  | |  | |   | | (____)| (__       _____   | |     | (___) | || || | (__     ')
print('   | |  |  __)    ) _ (    | |     (_____)  |  ___  | |   | ( (   ) |  __)  | (\ \) |  | |  | |   | |     __|  __)     (_____)  | | ____|  ___  | |(_)| |  __)    ')
print('   | |  | (      / ( ) \   | |              | (   ) | |   ) |\ \_/ /| (     | | \   |  | |  | |   | | (\ (  | (                 | | \_  | (   ) | |   | | (       ')
print('   | |  | (____/( /   \ )  | |              | )   ( | (__/  ) \   / | (____/| )  \  |  | |  | (___) | ) \ \_| (____/\           | (___) | )   ( | )   ( | (____/\ ')
print('   )_(  (_______|/     \|  )_(              |/     \(______/   \_/  (_______|/    )_)  )_(  (_______|/   \__(_______/           (_______|/     \|/     \(_______/ ')

title_screen()
