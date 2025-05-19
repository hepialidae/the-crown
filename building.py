import gamestate_tracking
from grid import *
from factions import *

class Building():
    def __init__(self, name, faction, cost):
        self.name = name
        self.faction = faction
        self.cost = cost
        self.built = False

    def build(self, row, column):
        self.built = True
        self.row = row
        self.column = column
        self.position = (row, column)
        gamestate_tracking.city_grounds[row][column].remove(" ")
        gamestate_tracking.city_grounds[row][column].append("x")
        gamestate_tracking.city_grounds[row][column].hold_building(self)


# buildings
class Palace(Building):
    def __init__(self):
        super().__init__("The Palace", "The Aether", 0)

class MagicLibrary(Building):
    def __init__(self):
        super().__init__("Magic Library", "The Arcanum", 1000)
    
    def donate_to(self, amount):
        if amount > 0:
            gamestate_tracking.treasury["currency"] -= amount
        else:
            raise Exception("Amount must be more than 0.") # remember to try-except this

class HolySpring(Building):
    def __init__(self):
        super().__init__("Holy Spring", "The Veiled", 1000)
    
    def worship(self):
        faction_dict["The Veiled"].modify_favor(10)