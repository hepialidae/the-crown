from may_change import faction_names, military_faction_name

faction_dict = {}
faction_opps = {
    "The Arcanum": "The Veiled",
    "The Veiled": "The Arcanum",
    "The Commoners": "The Gilded",
    "The Gilded": "The Commoners",
    "The Iron Guard": None
}

class Faction():
    def __init__(self, name):
        self.name = name
        self.favor = 50
        self.suspicion = 10
    
    def modify_suspicion(self, modifier):
        self.suspicion += modifier
    
    def modify_favor(self, modifier):
        self.favor += modifier

class IronGuard(Faction):
    def __init__(self):
        global military_faction_name
        super().__init__(military_faction_name)
        self.presence = 30
    
    def modify_presence(self, modifier):
        self.presence += modifier

# initialize factions
for name in faction_names:
    faction_dict[name] = Faction(name)
faction_dict[military_faction_name] = IronGuard()

def show_faction_stats():
    print("\n")
    for i in faction_names:
        print(f"{faction_dict[i].name}:")
        print(f"Favor: {faction_dict[i].favor}")
        print(f"Suspicion: {faction_dict[i].suspicion}\n")
    print(f"{military_faction_name}:")
    print(f"Presence: {faction_dict[military_faction_name].presence}")
    print(f"Suspicion: {faction_dict[military_faction_name].suspicion}\n")