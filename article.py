import random
from factions import faction_opps
from may_change import faction_names

class Article():
    def __init__(self):
        self.headline = ""
        self.contents = ""
    
    def define_impact(self):
        if self.impact == "suspicion":
            if self.mod >= 1: # positive mod
                return "negative"
            elif self.mod < 1: # negative mod
                return "positive"
        elif self.impact == "favor" or self.impact == "presence":
            if self.mod >= 1: # positive mod
                return "positive"
            elif self.mod < 1: # negative mod
                return "negative"
        else:
            raise Exception("Impact could not be defined")        


class ActionArticle(Article):
    def __init__(self, action, action_id, faction, impact, mod):
        super().__init__()
        self.action = action # type of action: decision, building, or interaction
        self.action_id = action_id # what the action does, like "new magic library". should come after "the"
        self.stance = random.choice(faction_names) # faction the author belongs to
        self.faction = faction # faction impacted by the action
        self.impact = impact # what stat was impacted
        self.mod = mod # whether the impact was positive or negative (building is always positive)
    
    def write(self):
        if self.stance == self.faction: # author belongs to faction affected
            if self.define_impact() == "positive":
                headlines = [
                    f"{self.faction} celebrates {self.action_id}", 
                    f"The {self.action_id}? A great idea!", 
                    f"{self.faction} welcomes {self.action_id}!",
                    f"The Emanator strikes again with the {self.action_id}!"
                ]
                self.headline = random.choice(headlines)
            elif self.define_impact() == "negative":
                headlines = [
                    f"The {self.action_id} is an insult to {self.stance}!"
                    f"{self.stance} condemns the {self.action_id}"
                ]
                self.headline = random.choice(headlines)
        elif self.stance == faction_opps[self.faction]: # author belongs to opposite faction
            if self.define_impact() == "positive":
                headlines = [
                    f"The {self.action_id} is an insult to {self.stance}!"
                    f"{self.stance} condemns the {self.action_id}"
                ]
                self.headline = random.choice(headlines)
            elif self.define_impact() == "negative":
                headlines = [
                    f"{self.stance} celebrates {self.action_id}", 
                    f"Suck it, {self.faction}, because the {self.action_id} is here!", 
                    f"{self.stance} welcomes {self.action_id}!",
                    f"The Emanator strikes again with the {self.action_id}!"
                ]
                self.headline = random.choice(headlines)
        else: # author is a neutral party
            headlines = [
                f"What will people think of the {self.action_id}?",
                f"The Emanator's reasoning behind the {self.action_id}"
            ]
            self.headline = random.choice(headlines)


class StateOfTheCityArticle(Article):
    def __init__(self, day):
        super().__init__()
        self.day = day
    
    def write(self):
        self.headline = f"State of the City: Day {self.day}"


class SillyArticle(Article):
    def __init__(self):
        super().__init__()
    
    def write(self):
        silly_headlines = [
            "Cat named Pizza runs out of pizza place, fears customers",
            "Florida man fights an alligator, loses"
        ]
        self.headline = random.choice(silly_headlines)