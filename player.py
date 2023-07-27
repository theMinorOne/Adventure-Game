
#Create Player Class
class Player():
    def __init__(self, name, race, pClass):
        #Player Attributes

        #Attributes for creation
        self.name = name
        self.race = race
        self.pClass = pClass

        #Attributes for gameplay
        self.baseHP = 100
        self.currHP = self.baseHP
        self.baseXP = 5
        self.xp = self.baseXP

        #Base stats
        self.baseAtk = 10
        self.currAtk = self.baseAtk

        self.baseDef = 10
        self.currDef = self.baseDef
        

    def displayTitle(self):
        return f"{self.name} the {self.race} {self.pClass}"
    
    def displayHP(self):
        return f"HP: {self.currHP}/{self.baseHP}"
    
    def displayXP(self):
        return f"XP: {self.xp}/{self.baseXP}"
    
    def displayStats(self):
        return f"{self.displayTitle()}\n{self.displayHP()}\n{self.displayXP()}"
