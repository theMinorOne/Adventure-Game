import random

type = ["Bandit", "Marauder", "Pirate", "Thief"]

#Create enemy class
class Enemy():
    def __init__(self, name, race, etype):
        pass
    #Enemy Attributes
        self.name = name
        self.race = race
        self.etype = etype

        # Attributes for gameplay
        self.baseHP = 100
        self.currHP = self.baseHP

        # Base stats
        self.baseAtk = 10
        self.currAtk = self.baseAtk

        self.baseDef = 10
        self.currDef = self.baseDef



    
    
 
