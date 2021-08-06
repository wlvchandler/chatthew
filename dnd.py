'''
Status: non-functional
testing out some D&D tools

Example module I/O:
roll 1d20         -> [16]
roll 2d20         -> [11, 9]
roll Nd20         -> [13, ..., 15] 
roll 1d20 2d6 3d8 -> [15, 3, 1, 1, 6, 8]
roll 5d6 best 3   -> [5, 3, 5]
roll 5d6 drop 2   -> [5, 3, 5] # Nd6 drop X has the same effect as Nd6 best (N-X)
'''

from random import randint
import math

# return list of rolls
def roll_die(sides=6, n=1):
    return [randint(1, sides) for x in range(n)]


class Stats():
    def __init__(self):
        self.STR = 10 # modifier = (stat - 10) / 2
        self.DEX = 10
        self.CON = 10
        self.INT = 10
        self.WIS = 10
        self.CHA = 10

class CharacterInfo():
    def __init__(self):
        self.race = None
        self.background = None
        self.height = None
        self.weight = None
        self.hairColor = None
        self.eyeColor = None
        self.alignment = None

class CharacterClass():
    def __init__(self):
        self.profBonus = 0
        self.startingItems = []
        
class Character():
    def __init__(self):
        self.player = None
        self.charInfo = CharacterInfo()
        self.stats = Stats()
        self.hitDie = None
        
class Dice():
    def __init__(self, sides=6):
        self.average = math.floor(sides / 2)
        
class Race():
    def __init__(self):
        self.statModifiers = [()] # (STR, 2);  (DEX, -1); etc
        self.vision = None
    

class Skill():
    skillStats = {
        'acrobatics'      : stats.DEX,
        'animal handling' : stats.WIS,
        'arcana'          : stats.INT,
        'athletics'       : stats.STR,
        'deception'       : stats.CHA,
        'history'         : stats.INT,
        'insight'         : stats.WIS,
        'intimidation'    : stats.CHA, 
        'investigation'   : stats.INT, 
        'medicine'        : stats.WIS, 
        'nature'          : stats.INT, 
        'perception'      : stats.WIS, 
        'performance'     : stats.CHA, 
        'persuasion'      : stats.CHA, 
        'religion'        : stats.INT, 
        'sleight of hand' : stats.DEX, 
        'stealth'         : stats.DEX, 
        'survival'        : stats.WIS
    }
    
    def __init__(self, skill=None, modifier=0, proficient=False):
        self.skill = skill.lower()
        self.stat = self.skillStats[self.skill]
        self.modifier = modifier
        self.proficient = proficient
