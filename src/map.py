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
        ZONENAME : 'Town Market',
        DESCRIPTION : 'This is your Local Marketplace',
        EXAMINATION : 'There is a vague smell of meat, herbs and fresh produce.',
        SOLVED : False,
        UP : 'a1',
        DOWN : 'b1',
        LEFT : 'a1',
        RIGHT : 'a2',
        DIALOGUE : 'A Seller in the Market says: "I used to go fishing at the beach, but now theres monsters nearby!"',
        ACTION : 'You are looking at the code'
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
        DIALOGUE : 'A old villager by the entrance says: "Hello my dear child, where have you come from?"',
        ACTION : 'The mayoral election are going on. Everyone is talking about it.'
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
        DIALOGUE : 'A villager by the Well in the middle says: "You should throw a gold coin in the well for good luck"',
        ACTION : 'I wish I could get good luck, but I dont have any money.'
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
        DIALOGUE : 'The Mayor comes out of the town hall. He says: "Beware all, for there are monsters south of here!"',
        ACTION : "There is a weird smell of rotten eggs inside. I'm not going inside!"
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
        DIALOGUE : 'Theres nobody to talk to here...',
        ACTION : 'You are looking at the code'
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
        DIALOGUE : '"Good luck on your journey.",Said your Mom .',
        ACTION : 'You are looking at the code'
    },
    'b3': {
        ZONENAME : 'Forest',
        DESCRIPTION : 'This is an oak forest.',
        EXAMINATION : 'This forest has a crossway so you can go any way you want',
        SOLVED : False,
        UP : 'a3',
        DOWN : 'c3',
        LEFT : 'b2',
        RIGHT : 'b4',
        DIALOGUE : '"I will give you a reward if you save to town from the monsters", said an old man',
        ACTION : 'You are looking at the code'
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
        DIALOGUE : 'Theres nobody to talk to here...',
        ACTION : 'You are looking at the code'
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
        DIALOGUE : 'Theres nobody to talk to here...',
        ACTION : 'You are looking at the code'
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
        DIALOGUE : 'Theres nobody to talk to here...',
        ACTION : 'You are looking at the code'
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
        DIALOGUE : 'Theres nobody to talk to here...',
        ACTION : 'You are looking at the code'
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
        DIALOGUE : 'Theres nobody to talk to here...',
        ACTION : 'You are looking at the code'
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
        DIALOGUE : 'Theres nobody to talk to here...',
        ACTION : 'The beach is too rocky to do anything.'
    },
    'd2': {
        ZONENAME : 'Beach',
        DESCRIPTION : 'This is a white, sandy Beach, with lots of children playing in the sand.',
        EXAMINATION : 'This beach has lots of children playing on it.',
        SOLVED : False,
        UP : 'c2',
        DOWN : 'd2',
        LEFT : 'd1',
        RIGHT : 'd3',
        DIALOGUE : '"my moomy sed dat da plase right of us is wery danegrus" said one of the children',
        ACTION : 'You are looking at the code'
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
        DIALOGUE : 'Theres nobody to talk to here...',
        ACTION : 'You are looking at the code'
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
        DIALOGUE : 'Theres nobody to talk to here...',
        ACTION : 'You are looking at the code'
    },
}
