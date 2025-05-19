from may_change import faction_names

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
faction_dict["The Iron Guard"] = IronGuard()