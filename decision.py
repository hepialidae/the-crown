from factions import *
from faction_stats import *
from decision_names import *

class Decision():
    # text is what is shown to the player
    # immediate is a bool value stating whether this happens immediately
    # effects must be lists containing tuples describing the effect: (faction_name, stat, modifier)
    def __init__(self, text, immediate, option_1_effects, option_2_effects):
        self.text = text
        self.mods = 0
        self.immediate = immediate
        self.option_1_effects = option_1_effects
        self.option_2_effects = option_2_effects
    
    def option_1(self):
        if self.immediate == True:
            for effect in self.option_1_effects:
                if effect[1] == "favor":
                    faction_dict[effect[0]].modify_favor(effect[2])
                elif effect[1] == "suspicion":
                    faction_dict[effect[0]].modify_suspicion(effect[2])
                elif effect[1] == "presence":
                    faction_dict[effect[0]].modify_presence(effect[2])
        elif self.immediate == False:
            pass # I have no idea genuinely
        update_stats()
        return None
    
    def option_2(self):
        if self.immediate == True:
            for effect in self.option_2_effects:
                if effect[1] == "favor":
                    faction_dict[effect[0]].modify_favor(effect[2])
                elif effect[1] == "suspicion":
                    faction_dict[effect[0]].modify_suspicion(effect[2])
                elif effect[1] == "presence":
                    faction_dict[effect[0]].modify_presence(effect[2])
        elif self.immediate == False:
            pass
        update_stats()
        return None