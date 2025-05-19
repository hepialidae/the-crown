from factions import *
from may_change import *
import gamestate_tracking
from tutorial import sleep

def afternoon():
    gamestate_tracking.treasury["currency"] += tax_per_day
    print(f"\n{secretary_title}: Good afternoon, {gamestate_tracking.player_name}.")
    sleep(0.8)
    print(f"{secretary_title}: You may develop the city using the resources you have.")
    sleep()
    print(f"{secretary_title}: You have {gamestate_tracking.treasury['currency']} coins.")