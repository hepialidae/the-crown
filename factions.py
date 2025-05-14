faction_list = []

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
        super().__init__("The Iron Guard")
        self.presence = 30
    
    def modify_presence(self, modifier):
        self.precense += modifier