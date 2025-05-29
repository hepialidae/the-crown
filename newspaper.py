import gamestate_tracking

newspaper = []

class Article():
    def __init__(self, action, stance, faction, impact, impact_type):
        self.action = action # type of action: decision, building, or interaction
        self.stance = stance # the writer's stance towards the player (positive or negative)
        self.faction = faction # faction impacted by the action
        self.impact = impact # what stat was impacted
        self.impact_type = impact_type # whether the impact was positive or negative (building is always positive)
    
    def write(self):
        headline = ""