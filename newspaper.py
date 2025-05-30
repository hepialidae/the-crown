import gamestate_tracking
from tutorial import sleep
from article import ActionArticle, SillyArticle, StateOfTheCityArticle

# 5 newspaper articles total
# CONTENTS: 3 on today's actions, 1 on state of the city, 1 silly :3
# should add a function for getting the info for article inits

class Newspaper():
    def __init__(self):
        self.action_articles = list()
        self.final_articles = list()
    
    def add_article(self, article, type):
        if type == "action":
            self.action_articles.append(article)
        else:
            self.final_articles.append(article)
    
    def add_action_article(self, action, action_id, faction, impact, mod):
        article = ActionArticle(action, action_id, faction, impact, mod)
        article.write()
        self.add_article(article, "action")
    
    def add_silly_article(self):
        article = SillyArticle()
        article.write()
        self.add_article(article, "silly")
    
    def add_state_of_the_city_article(self):
        article = StateOfTheCityArticle(gamestate_tracking.day)
        article.write()
        self.add_article(article, "state of the city")