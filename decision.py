from factions import *
import gamestate_tracking
from decision_names import *

class Decision():
    # text is what is shown to the player
    # immediate is a bool value stating whether this happens immediately
    # effects must be lists containing tuples describing the effect: (faction_name, stat, modifier)
    def __init__(self, text, immediate, option_1_effects, option_2_effects, id):
        self.text = text
        self.immediate = immediate
        self.option_1_effects = option_1_effects
        self.option_2_effects = option_2_effects
        self.id = id
    
    def option_1(self):
        if self.immediate == True:
            newspaper = gamestate_tracking.todays_newspaper
            for effect in self.option_1_effects:
                if effect[1] == "favor":
                    faction_dict[effect[0]].modify_favor(effect[2])
                elif effect[1] == "suspicion":
                    faction_dict[effect[0]].modify_suspicion(effect[2])
                elif effect[1] == "presence":
                    faction_dict[effect[0]].modify_presence(effect[2])
                newspaper.add_action_article("decision", self.id, effect[0], effect[1], effect[2])
        elif self.immediate == False:
            pass # I have no idea genuinely
        return None
    
    def option_2(self):
        if self.immediate == True:
            newspaper = gamestate_tracking.todays_newspaper
            for effect in self.option_2_effects:
                if effect[1] == "favor":
                    faction_dict[effect[0]].modify_favor(effect[2])
                elif effect[1] == "suspicion":
                    faction_dict[effect[0]].modify_suspicion(effect[2])
                elif effect[1] == "presence":
                    faction_dict[effect[0]].modify_presence(effect[2])
                newspaper.add_action_article("decision", self.id, effect[0], effect[1], effect[2])
        elif self.immediate == False:
            pass
        return None