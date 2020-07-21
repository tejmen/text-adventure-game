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

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False, 'a5': False,
                'b1': False, 'b2': False, 'b3': False, 'b4': False, 'b5': False,
                'c1': False, 'c2': False, 'c3': False, 'c4': False, 'c5': False,
                }

zonemap = {
    'a1': {
        ZONENAME : 'Chest',
        DESCRIPTION : 'This is an unlocked chest!',
        EXAMINATION : 'The key is already in the Chest lock.',
        SOLVED : False,
        UP : 'a1',
        DOWN : 'b1',
        LEFT : 'a1',
        RIGHT : 'a2',
        DIALOGUE : 'Nobody is here',
        ACTION : 'You are looking at the code'
    },
    'a2': {
        ZONENAME : 'Bridge',
        DESCRIPTION : 'This is a bridge',
        EXAMINATION : 'I could play pooh sticks on this bridge.',
        SOLVED : False,
        UP : 'a2',
        DOWN : 'b2',
        LEFT : 'a1',
        RIGHT : 'a3',
        DIALOGUE : 'Nobody is here',
        ACTION : 'You are looking at the code'
    },
    'a3': {
        ZONENAME : 'Spikes',
        DESCRIPTION : 'These are thorny bushes',
        EXAMINATION : 'I take damage off these bushes',
        SOLVED : False,
        UP : 'a3',
        DOWN : 'b3',
        LEFT : 'a2',
        RIGHT : 'a4',
        DIALOGUE : 'Nobody is here',
        ACTION : 'You are looking at the code'
    },
    'a4': {
        ZONENAME : 'Spikes',
        DESCRIPTION : 'These are thorny bushes',
        EXAMINATION : 'I take damage off these bushes',
        SOLVED : False,
        UP : 'a4',
        DOWN : 'b4',
        LEFT : 'a3',
        RIGHT : 'a5',
        DIALOGUE : 'Nobody is here!',
        ACTION : 'You are looking at the code'
    },
    'a5': {
        ZONENAME : 'Dungeon',
        DESCRIPTION : 'This is a dangerous Dungeon.',
        EXAMINATION : 'This Dungeon has dangers. Mum said to stay away from dangerous places.',
        SOLVED : False,
        UP : 'a5',
        DOWN : 'b5',
        LEFT : 'a4',
        RIGHT : 'a5',
        DIALOGUE : 'Theres nobody to talk to here...',
        ACTION : 'You are looking at the code'
    },
    'b1': {
        ZONENAME : 'Farm House',
        DESCRIPTION : "This is somebody's house",
        EXAMINATION : 'There are people living here',
        SOLVED : False,
        UP : 'a1',
        DOWN : 'c1',
        LEFT : 'b1',
        RIGHT : 'b2',
        DIALOGUE : "'You can't go across the bridges, dangers are there' said the farm owner",
        ACTION : 'You are looking at the code'
    },
    'b2': {
        ZONENAME : 'Bridge',
        DESCRIPTION : 'This is a bridge',
        EXAMINATION : 'I could play pooh sticks on this bridge.',
        SOLVED : False,
        UP : 'a2',
        DOWN : 'c2',
        LEFT : 'b1',
        RIGHT : 'b3',
        DIALOGUE : 'Nobody is here',
        ACTION : 'You are looking at the code'
    },
    'b3': {
        ZONENAME : 'Spikes',
        DESCRIPTION : 'These are thorny bushes',
        EXAMINATION : 'I take damage off these bushes',
        SOLVED : False,
        UP : 'a3',
        DOWN : 'c3',
        LEFT : 'b2',
        RIGHT : 'b4',
        DIALOGUE : 'Nobody is here!',
        ACTION : 'You are looking at the code'
    },
    'b4': {
        ZONENAME : 'Dungeon',
        DESCRIPTION : 'This is a dangerous Dungeon.',
        EXAMINATION : 'This Dungeon has dangers. Mum said to stay away from dangerous places.',
        SOLVED : False,
        UP : 'a4',
        DOWN : 'c4',
        LEFT : 'b3',
        RIGHT : 'b5',
        DIALOGUE : 'Theres nobody to talk to here...',
        ACTION : 'You are looking at the code'
    },
    'b5': {
        ZONENAME : 'End Portal',
        DESCRIPTION : 'This is where you go if you want to stop exploring.',
        EXAMINATION : 'This is a way to go to the main menu.',
        SOLVED : False,
        UP : 'a5',
        DOWN : 'c5',
        LEFT : 'b3',
        RIGHT : 'b5',
        DIALOGUE : 'Theres nobody to talk to here...',
        ACTION : 'You are looking at the code'
    },
    'c1': {
        ZONENAME : 'Farmland',
        DESCRIPTION : 'There is some farmland in this area',
        EXAMINATION : 'The crops are growing perfectly',
        SOLVED : False,
        UP : 'b1',
        DOWN : 'c1',
        LEFT : 'c1',
        RIGHT : 'c2',
        DIALOGUE : '"You can eat some of the crops if you want"',
        ACTION : 'You are looking at the code'
    },
    'c2': {
        ZONENAME : 'Bridge',
        DESCRIPTION : 'This is a bridge',
        EXAMINATION : 'I could play pooh sticks on this bridge.',
        SOLVED : False,
        UP : 'b2',
        DOWN : 'c2',
        LEFT : 'c1',
        RIGHT : 'c3',
        DIALOGUE : 'Nobody is here',
        ACTION : 'You are looking at the code'
    },
    'c3': {
        ZONENAME : 'Spikes',
        DESCRIPTION : 'These are thorny bushes',
        EXAMINATION : 'I take damage off these bushes',
        SOLVED : False,
        UP : 'b3',
        DOWN : 'c3',
        LEFT : 'c2',
        RIGHT : 'c4',
        DIALOGUE : 'Nobody is here!',
        ACTION : 'You are looking at the code'
    },
    'c4': {
        ZONENAME : 'Spikes',
        DESCRIPTION : 'These are thorny bushes',
        EXAMINATION : 'I take damage off these bushes',
        SOLVED : False,
        UP : 'b3',
        DOWN : 'c4',
        LEFT : 'c2',
        RIGHT : 'c5',
        DIALOGUE : 'Nobody is here!',
        ACTION : 'You are looking at the code'
    },
    'c5': {
        ZONENAME : 'Dungeon',
        DESCRIPTION : 'This is a dangerous Dungeon.',
        EXAMINATION : 'This Dungeon has dangers. Mum said to stay away from dangerous places.',
        SOLVED : False,
        UP : 'b5',
        DOWN : 'c5',
        LEFT : 'c4',
        RIGHT : 'a5',
        DIALOGUE : 'Theres nobody to talk to here...',
        ACTION : 'You are looking at the code'
    },
}
