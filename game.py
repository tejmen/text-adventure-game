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
class Player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
myPlayer = Player()