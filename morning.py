import random as rand
from decision import *
from factions import *
from may_change import *
import gamestate_tracking
from tutorial import sleep
from decision_names import *
from newspaper import Newspaper

def morning():
    global decision_names, secretary_title
    gamestate_tracking.todays_newspaper = Newspaper()
    print(f"{secretary_title}: Good morning, {gamestate_tracking.player_name}.")
    sleep()
    print(f"{secretary_title}: It is now day {gamestate_tracking.day} of your reign.")
    sleep()
    requests = rand.randint(3, 7)
    print(f"{secretary_title}: You have {requests} requests to review this morning.")
    sleep()
    for i in range(requests):
        print(f"\n{secretary_title}: Here is request number {i + 1}.")
        sleep()
        decision_num = rand.randint(0, len(decision_names) - 1)
        decision = Decision(decision_names[decision_num][0], decision_names[decision_num][1], decision_names[decision_num][2], decision_names[decision_num][3], decision_names[decision_num][4])
        appropriate_choice = False
        while appropriate_choice == False:
            print(f"{secretary_title}: {decision.text}")
            sleep()
            choice = input(f"{secretary_title}: Enter A or B to make your choice: ")
            if choice.lower() == "a":
                decision.option_1()
                appropriate_choice = True
            elif choice.lower() == "b":
                decision.option_2()
                appropriate_choice = True
            else:
                print(f"\n{secretary_title}: Invalid choice. Please enter A or B.\n")
                sleep(0.5)
        show_faction_stats()
    print(f"{secretary_title}: This is the end of the morning phase.")
    gamestate_tracking.phase = 2
    sleep(3)
    return None