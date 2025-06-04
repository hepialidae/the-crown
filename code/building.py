from grid import *
from factions import *
from may_change import *
import gamestate_tracking

building_dict = {}

class Building():
    def __init__(self, name, id, faction, cost):
        self.name = name
        self.id = id
        self.faction = faction
        self.cost = cost
        self.built = False
        building_dict[id] = self
        self.interactions = None

    def build(self, row, column):
        self.built = True
        self.row = row
        self.column = column
        self.position = (row, column)
        gamestate_tracking.city_grounds[row][column].hold_building(self)
        gamestate_tracking.treasury["currency"] -= self.cost
    
    def interaction1():
        pass

    def interaction2():
        pass

# buildings
class Palace(Building):
    def __init__(self):
        super().__init__("Palace", "palace", "The Aether", 0)

class MagicLibrary(Building):
    def __init__(self):
        super().__init__("Magic Library", "magic library", "The Arcanum", 1000)
        self.interactions = ["donate to the Magic Library"]

    def donate_to(self, amount=0):
        if amount > 0:
            gamestate_tracking.treasury["currency"] -= amount
        else:
            raise Exception("Amount must be more than 0.") # remember to try-except this
        faction_dict["The Arcanum"].modify_favor(10)
    
    def interaction1(self):
        while True:
            donation_amount = int(input(f"\n{secretary_title}: How much would you like to donate? Enter the number of coins: "))
            try:
                self.donate_to(donation_amount)
                print(f"{secretary_title}: Your donation pleases the Arcanum.")
                return None
            except Exception:
                print(f"\n{secretary_title}: Please enter a number above 0.")

class HolySpring(Building):
    def __init__(self):
        super().__init__("Holy Spring", "holy spring", "The Veiled", 1000)
        self.interactions = ["worship the Holy Spring"]
    
    def worship(self):
        faction_dict["The Veiled"].modify_favor(10)
    
    def interaction1(self):
        self.worship()
        print(f"{secretary_title}: Your open worship pleases the Veiled.")

def find_buildable_buildings():
    buildable_buildings = []
    for building in building_dict.values():
        if not building.built:
            buildable_buildings.append(building.name)
    return ", ".join(buildable_buildings)

# init code
def init_buildings():
    palace = Palace()
    palace.build(2, 2)

    MagicLibrary()

    HolySpring()

    return None

init_buildings()