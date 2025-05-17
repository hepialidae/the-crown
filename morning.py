from tutorial import sleep
from decision import *
from factions import *
from gamestate_tracking import *
from names import *
from decision_names import *
import random as rand
from faction_stats import create_stats_window

def morning():
    global decision_names, secretary_title, player_name, day
    print(f"{secretary_title}: Good morning, {player_name}.")
    sleep()
    print(f"{secretary_title}: It is now day {day} of your reign.")
    sleep()
    requests = rand.randint(2, 5)
    print(f"{secretary_title}: You have {requests} requests to review this morning.")
    sleep()
    for i in range(requests):
        print(f"{secretary_title}: Here is request number {i + 1}.")
        sleep()
        decision_num = rand.randint(0, len(decision_names) - 1)
        decision = Decision(decision_names[decision_num][0], decision_names[decision_num][1], decision_names[decision_num][2], decision_names[decision_num][3])
        print(f"{secretary_title}: {decision.text}")
        sleep()
        choice = input(f"{secretary_title}: Enter A or B to make your choice: ")
        if choice.lower() == "a":
            decision.option_1()
        elif choice.lower() == "b":
            decision.option_2()
        else:
            print(f"{secretary_title}: Invalid choice. Please enter A or B.")
            sleep()
            i -= 1
    print(f"{secretary_title}: This is the end of the morning phase.")
    return None