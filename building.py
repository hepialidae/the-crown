import gamestate_tracking
from grid import *
from factions import *

building_dict = {}

class Building():
    def __init__(self, name, id, faction, cost):
        self.name = name
        self.id = id
        self.faction = faction
        self.cost = cost
        self.built = False
        building_dict[name] = self

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
        super().__init__("The Palace", "the palace", "The Aether", 0)

class MagicLibrary(Building):
    def __init__(self):
        super().__init__("Magic Library", "magic library", "The Arcanum", 1000)

    def donate_to(self, amount):
        if amount > 0:
            gamestate_tracking.treasury["currency"] -= amount
        else:
            raise Exception("Amount must be more than 0.") # remember to try-except this

class HolySpring(Building):
    def __init__(self):
        super().__init__("Holy Spring", "holy spring", "The Veiled", 1000)
    
    def worship(self):
        faction_dict["The Veiled"].modify_favor(10)