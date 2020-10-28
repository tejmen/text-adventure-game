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

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False,
                 }

zonemap = {
    'a1': {
        ZONENAME: 'Town Market',
        DESCRIPTION: 'This is your Local Marketplace',
        EXAMINATION: 'There is a vague smell of meat, herbs and fresh produce.',
        SOLVED: False,
        UP: 'null',
        DOWN: 'b1',
        LEFT: 'null',
        RIGHT: 'a2',
        DIALOGUE: 'A Seller in the Market says: "I used to go fishing at the beach, but now theres monsters nearby!"',
        ACTION: '''
if myPlayer.money == 0:
    print1 = '"Go get money so you can buy stuff!" shouts one of the merchants'
    for character in print1:
        sys.stdout.write(character)
        sys.stdout.flush()
    time.sleep(0.1)
else:
    shop()
        '''
    },
    'a2': {
        ZONENAME: 'Town Entrance',
        DESCRIPTION: 'This is an entrance to your Town.',
        EXAMINATION: 'The angel on the top symbolizes that your village is peaceful.',
        SOLVED: False,
        UP: 'null',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
        DIALOGUE: 'A old villager by the entrance says: "Hello my dear child, where have you come from?"',
        ACTION: '''print("The mayoral election are going on. Everyone is talking about it.")'''
    },
    'a3': {
        ZONENAME: 'Town Square',
        DESCRIPTION: 'This is your Town Square.',
        EXAMINATION: 'There is a wishing well in the middle.',
        SOLVED: False,
        UP: 'null',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
        DIALOGUE: 'A villager by the Well in the middle says: "You should throw a gold coin in the well for good luck"',
        ACTION: 'I wish I could get good luck, but I dont have any money.'
    },
    'a4': {
        ZONENAME: 'Town Hall',
        DESCRIPTION: 'This is where the mayor lives',
        EXAMINATION: 'Mum said "This Building has a prison for baddies!"',
        SOLVED: False,
        UP: 'null',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: 'null',
        DIALOGUE: 'The Mayor comes out of the town hall. He says: "Beware all, for there are monsters south of here!"',
        ACTION: """print("There is a weird smell of rotten eggs inside. I'm not going inside!")"""
    },
    'b1': {
        ZONENAME: 'Chest',
        DESCRIPTION: 'This is an unlocked chest!',
        EXAMINATION: 'The key is already in the Chest lock.',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: 'null',
        RIGHT: 'b2',
        DIALOGUE: 'Theres nobody to talk to here...',
        ACTION: '''
print('You pick up the knife')
myPlayer.inventory.append('knife')
        '''
    },
    'b2': {
        ZONENAME: 'Home',
        DESCRIPTION: 'This is your home!',
        EXAMINATION: 'Your home is the same - nothing has changed',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
        DIALOGUE: '"Good luck on your journey.",Said your Mom .',
        ACTION: '''
print1 = 'You take a nap'
myPlayer.hp = myPlayer.max
for character in print1:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.1)
time.sleep(1)
        '''
    },
    'b3': {
        ZONENAME: 'Forest',
        DESCRIPTION: 'This is an oak forest.',
        EXAMINATION: 'This forest has a crossway so you can go any way you want',
        SOLVED: False,
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4',
        DIALOGUE: '"I will give you a reward if you save to town from the monsters", said an old man',
        ACTION: '''
if myPlayer.xp == 0:
    print1 = '"I will give you some money if you defeat the monsters south of here" said an old man.'
    for character in print1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
else:
    print1 = "I have given you some money."
    print2 = "Now go away!"
    for character in print1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    print('')
    for character in print2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    myPlayer.money = myPlayer.money + 40
    map.zonemap[myPlayer.location][SOLVED] = True
time.sleep(1)
        '''
    },
    'b4': {
        ZONENAME: '???',
        DESCRIPTION: 'This is an old Building.',
        EXAMINATION: 'There is a button and a glowing circle on the floor.',
        SOLVED: False,
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: 'null',
        DIALOGUE: 'Theres nobody to talk to here...',
        ACTION: '''
myPlayer.location = 'c1'
map.zonemap[myPlayer.location][ZONENAME] = 'Telporter'
map.zonemap['b4'][ZONENAME] = 'Telporter'
destination = myPlayer.location
movement_handler(destination)
        '''
    },
    'c1': {
        ZONENAME: '???',
        DESCRIPTION: 'This is an old Building.',
        EXAMINATION: 'There is a button and a circle on the floor.',
        SOLVED: False,
        UP: 'b1',
        DOWN: 'd1',
        LEFT: 'null',
        RIGHT: 'c2',
        DIALOGUE: 'Theres nobody to talk to here...',
        ACTION: '''
myPlayer.location = 'b4'
map.zonemap['c1'][ZONENAME] = 'Telporter'
destination = myPlayer.location
movement_handler(destination)
            '''
    },
    'c2': {
        ZONENAME: 'Forest',
        DESCRIPTION: 'This is an ash forest.',
        EXAMINATION: 'This forest has a crossway so you can go any way you want',
        SOLVED: False,
        UP: 'b2',
        DOWN: 'd2',
        LEFT: 'c1',
        RIGHT: 'c3',
        DIALOGUE: 'Theres nobody to talk to here...',
        ACTION: '''
if map.zonemap['c1'][ZONENAME] == 'Telporter':
    print("'Thank you for finding out what that place was! I'll give you a reward for doing that'said the mysterious man, giving you some money.")
    myPlayer.money = myPlayer.money + 30
    map.zonemap[myPlayer.location][SOLVED] = True
else:
    print('"Can you please find;  out what is in the place left of us.I really want to live there" said a mysterious man')
        '''
    },
    'c3': {
        ZONENAME: 'Forest',
        DESCRIPTION: 'This is a birch forest.',
        EXAMINATION: 'This forest has a crossway so you can go any way you want.',
        SOLVED: False,
        UP: 'b3',
        DOWN: 'd3',
        LEFT: 'c2',
        RIGHT: 'c4',
        DIALOGUE: 'Theres nobody to talk to here...',
        ACTION: '''
print1 = 'You take a nap'
myPlayer.hp = myPlayer.max
for character in print1:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.1)
time.sleep(1)
        '''
    },
    'c4': {
        ZONENAME: 'Dungeon',
        DESCRIPTION: 'This is a dangerous Dungeon.',
        EXAMINATION: 'This Dungeon has dangers. Mum said to stay away from dangerous places.',
        SOLVED: False,
        UP: 'b4',
        DOWN: 'd4',
        LEFT: 'c3',
        RIGHT: 'null',
        DIALOGUE: 'Theres nobody to talk to here...',
        ACTION: '''turn_based_combat()'''
    },
    'd1': {
        ZONENAME: 'Beach',
        DESCRIPTION: 'This is a rocky beach',
        EXAMINATION: 'This beach has lots of seaweed.',
        SOLVED: False,
        UP: 'c1',
        DOWN: 'null',
        LEFT: 'null',
        RIGHT: 'd2',
        DIALOGUE: 'Theres nobody to talk to here...',
        ACTION: '''print('The beach is too rocky to do anything.')'''
    },
    'd2': {
        ZONENAME: 'Beach',
        DESCRIPTION: 'This is a white, sandy Beach, with lots of children playing in the sand.',
        EXAMINATION: 'This beach has lots of children playing on it.',
        SOLVED: False,
        UP: 'c2',
        DOWN: 'null',
        LEFT: 'd1',
        RIGHT: 'd3',
        DIALOGUE: '"my moomy sed dat da plase right of us is wery danegrus" said one of the children',
        ACTION: '''
print1 = 'this beach is so sandy that... '
print2 = ' you take a nap.'
myPlayer.hp = myPlayer.max
for character in print1:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.1)
print('')
for character in print2:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.1)
time.sleep(1)
        '''
    },
    'd3': {
        ZONENAME: 'Dungeon',
        DESCRIPTION: 'This is a dangerous Dungeon.',
        EXAMINATION: 'This Dungeon has dangers. Mum said to stay away from dangerous places.',
        SOLVED: False,
        UP: 'c3',
        DOWN: 'null',
        LEFT: 'd2',
        RIGHT: 'd4',
        DIALOGUE: 'Theres nobody to talk to here...',
        ACTION: '''turn_based_combat()'''
    },
    'd4': {
        ZONENAME: 'End Portal',
        DESCRIPTION: 'This is where you go if you want to leave this world.',
        EXAMINATION: 'This is a way to go to a whole new world.',
        SOLVED: False,
        UP: 'c4',
        DOWN: 'null',
        LEFT: 'd3',
        RIGHT: 'null',
        DIALOGUE: 'Theres nobody to talk to here...',
        ACTION: '''
# New_Map()
myPlayer.location = 'e1'
destination = myPlayer.location
movement_handler(destination)
        '''
    },
    'e1': {
        ZONENAME: 'Chest',
        DESCRIPTION: 'This is an unlocked chest!',
        EXAMINATION: 'There is no key in the Chest lock.',
        SOLVED: False,
        UP: 'null',
        DOWN: 'f1',
        LEFT: 'null',
        RIGHT: 'e2',
        DIALOGUE: 'Nobody is here',
        ACTION: '''
if 'key' in myPlayer.inventory:
    print('You pick up the shield.')
    myPlayer.inventory.append('shield')
else:
    print('You NEED A KEY!')
        '''
    },
    'e2': {
        ZONENAME: 'Bridge',
        DESCRIPTION: 'This is a bridge',
        EXAMINATION: 'I could play pooh sticks on this bridge.',
        SOLVED: False,
        UP: 'null',
        DOWN: 'f2',
        LEFT: 'e1',
        RIGHT: 'e3',
        DIALOGUE: 'Nobody is here',
        ACTION: '''print('I wish I could play pooh sticks, but I have no one to play with me.')'''
    },
    'e3': {
        ZONENAME: 'Spikes',
        DESCRIPTION: 'These are thorny bushes',
        EXAMINATION: 'I take damage of these bushes',
        SOLVED: True,
        UP: 'null',
        DOWN: 'f3',
        LEFT: 'e2',
        RIGHT: 'e4',
        DIALOGUE: 'Nobody is here',
        ACTION: '''print('Theres nothing to do here')'''
    },
    'e4': {
        ZONENAME: 'Spikes',
        DESCRIPTION: 'These are thorny bushes',
        EXAMINATION: 'I take damage of these bushes',
        SOLVED: True,
        UP: 'null',
        DOWN: 'f4',
        LEFT: 'e3',
        RIGHT: 'e5',
        DIALOGUE: 'Nobody is here!',
        ACTION: '''print('Theres nothing to do here')'''
    },
    'e5': {
        ZONENAME: 'Dungeon',
        DESCRIPTION: 'This is a dangerous Dungeon.',
        EXAMINATION: 'This Dungeon has dangers. Mum said to stay away from dangerous places.',
        SOLVED: False,
        UP: 'null',
        DOWN: 'f5',
        LEFT: 'e4',
        RIGHT: 'null',
        DIALOGUE: 'Theres nobody to talk to here...',
        ACTION: '''turn_based_combat()'''
    },
    'f1': {
        ZONENAME: 'Farm House',
        DESCRIPTION: "This is somebody's house",
        EXAMINATION: 'There are people living here',
        SOLVED: False,
        UP: 'e1',
        DOWN: 'g1',
        LEFT: 'null',
        RIGHT: 'f2',
        DIALOGUE: "'You can't go across the bridges, dangers are there' said the farm owner",
        ACTION: '''
print1 = 'You take a nap'
myPlayer.hp = myPlayer.max
for character in print1:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.1)
time.sleep(1)
        '''
    },
    'f2': {
        ZONENAME: 'Bridge',
        DESCRIPTION: 'This is a bridge',
        EXAMINATION: 'I could play pooh sticks on this bridge.',
        SOLVED: False,
        UP: 'e2',
        DOWN: 'g2',
        LEFT: 'f1',
        RIGHT: 'f3',
        DIALOGUE: 'Nobody is here',
        ACTION: '''print('I wish I could play pooh sticks, but I have no one to play with me.')'''
    },
    'f3': {
        ZONENAME: 'Spikes',
        DESCRIPTION: 'These are thorny bushes',
        EXAMINATION: 'I take damage of these bushes',
        SOLVED: True,
        UP: 'e3',
        DOWN: 'g3',
        LEFT: 'f2',
        RIGHT: 'f4',
        DIALOGUE: 'Nobody is here!',
        ACTION: '''print('Theres nothing to do here')'''
    },
    'f4': {
        ZONENAME: 'Dungeon',
        DESCRIPTION: 'This is a dangerous Dungeon.',
        EXAMINATION: 'This Dungeon has dangers. Mum said to stay away from dangerous places.',
        SOLVED: False,
        UP: 'e4',
        DOWN: 'g4',
        LEFT: 'f3',
        RIGHT: 'f5',
        DIALOGUE: 'Theres nobody to talk to here...',
        ACTION: '''turn_based_combat()'''
    },
    'f5': {
        ZONENAME: 'End Portal',
        DESCRIPTION: 'This is where you go if you want to stop exploring.',
        EXAMINATION: 'This is a way to go to the main menu.',
        SOLVED: False,
        UP: 'e5',
        DOWN: 'g5',
        LEFT: 'f3',
        RIGHT: 'null',
        DIALOGUE: 'Theres nobody to talk to here...',
        ACTION: '''title_screen()'''
    },
    'g1': {
        ZONENAME: 'Farmland',
        DESCRIPTION: 'There is some farmland in this area',
        EXAMINATION: 'The corn are growing perfectly',
        SOLVED: False,
        UP: 'f1',
        DOWN: 'null',
        LEFT: 'null',
        RIGHT: 'g2',
        DIALOGUE: '"You can eat some of the corn if you want"',
        ACTION: '''
print1 = 'You eat some corn.'
myPlayer.hp = myPlayer.max
for character in print1:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
time.sleep(0.2)
        '''
    },
    'g2': {
        ZONENAME: 'Bridge',
        DESCRIPTION: 'This is a bridge',
        EXAMINATION: 'I could play pooh sticks on this bridge.',
        SOLVED: False,
        UP: 'f2',
        DOWN: 'null',
        LEFT: 'g1',
        RIGHT: 'g3',
        DIALOGUE: 'Nobody is here',
        ACTION: '''print('I wish I could play pooh sticks, but I have no one to play with me')'''
    },
    'g3': {
        ZONENAME: 'Spikes',
        DESCRIPTION: 'These are thorny bushes',
        EXAMINATION: 'I take damage of these bushes',
        SOLVED: True,
        UP: 'f3',
        DOWN: 'null',
        LEFT: 'g2',
        RIGHT: 'e4',
        DIALOGUE: 'Nobody is here!',
        ACTION: '''print('Theres nothing to do here')'''
    },
    'g4': {
        ZONENAME: 'Spikes',
        DESCRIPTION: 'These are thorny bushes',
        EXAMINATION: 'I take damage of these bushes',
        SOLVED: True,
        UP: 'f3',
        DOWN: 'null',
        LEFT: 'g2',
        RIGHT: 'e5',
        DIALOGUE: 'Nobody is here!',
        ACTION: '''print('Theres nothing to do here')'''
    },
    'g5': {
        ZONENAME: 'Dungeon',
        DESCRIPTION: 'This is a dangerous Dungeon.',
        EXAMINATION: 'This Dungeon has dangers. Mum said to stay away from dangerous places.',
        SOLVED: False,
        UP: 'f5',
        DOWN: 'null',
        LEFT: 'g4',
        RIGHT: 'null',
        DIALOGUE: 'Nobody is here!',
        ACTION: '''turn_based_combat()'''
    },
}
