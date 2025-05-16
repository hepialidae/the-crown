from names import *

faction_dict = {}

class Faction():
    def __init__(self, name):
        self.name = name
        self.favor = 50
        self.suspicion = 10
    
    def modify_suspicion(self, modifier):
        self.suspicion += modifier
    
    def modify_favor(self, modifier):
        self.favor += modifier

class Iron_Guard(Faction):
    def __init__(self):
        global military_faction_name
        super().__init__(military_faction_name)
        self.presence = 30
    
    def modify_presence(self, modifier):
        self.precense += modifier

def show_faction_stats():
    global faction_list
    for faction in faction_list:
        print(f"{faction.name}:")
        if faction.name == "The Iron Guard":
            print(f"Military Presence: {faction.presence}")
        else:
            print(f"Favor: {faction.favor}")
        print(f"Suspicion: {faction.suspicion}\n")

# initialize factions
for name in faction_names:
    faction_dict[name] = Faction(name)
faction_dict["The Iron Guard"] = Iron_Guard()
print(faction_dict)