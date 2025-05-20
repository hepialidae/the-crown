from factions import *
from building import *
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
    sleep()
    choice = None
    while choice != "exit":
        print(f"\n{secretary_title}: Enter '1' to build a building.")
        sleep(0.5)
        print(f"{secretary_title}: Enter '2' to interact with a building on the grid.")
        sleep(0.5)
        print(f"{secretary_title}: Enter '3' to check your treasury.")
        sleep(0.5)
        print(f"{secretary_title}: Enter 'Exit' to exit this phase.")
        sleep(0.5)
        choice = input(f"{secretary_title}: What would you like to do? ").lower().strip()
        if choice == "1":
            print(gamestate_tracking.city_grounds)
        elif choice == "2":
            pass
        elif choice == "3":
            print(f"\n{secretary_title}: You have {gamestate_tracking.treasury['currency']} coins.")
            sleep()
        elif choice == "exit":
            sleep()
            gamestate_tracking.phase = 3
            return None

afternoon()