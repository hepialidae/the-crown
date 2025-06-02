from factions import *
import gamestate_tracking
from tutorial import sleep

def check_endings():
    if faction_dict["The Commoners"].favor <= 20 and faction_dict["The Iron Guard"].presence <= 20: # commoner riot ending
        print(f"\n<ENDING 1>")
        sleep(0.8)
        print("<The Commoners are unhappy with their treatment.>")
        sleep()
        print("<They riot, and the Iron Guard is unable to stop them.>")
        sleep()
        print("<The city is in chaos, and you are executed by the mob.>\n")
        gamestate_tracking.phase = 4


# ENDING PLANNING:
# 6 main endings, lean into one faction/balance -> what if the player leans into two factions?
# 3 phases for each ending, tracked in gamestate_tracking.py
# Academocracy/meritocracy: 
# Theocracy:
# Communist dictatorship:
# Authoritarian dictatorship: 
# Plutocracy: