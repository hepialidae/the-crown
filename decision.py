from decision_names import *
from factions import *

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
        pass