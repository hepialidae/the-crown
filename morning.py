from tutorial import sleep
from decision import *
from factions import *
import gamestate_tracking
from may_change import *
from decision_names import *
import random as rand
from faction_stats import create_stats_window

def morning():
    global decision_names, secretary_title
    print(f"{secretary_title}: Good morning, {gamestate_tracking.player_name}.")
    sleep()
    print(f"{secretary_title}: It is now day {gamestate_tracking.day} of your reign.")
    sleep()
    requests = rand.randint(2, 5)
    print(f"{secretary_title}: You have {requests} requests to review this morning.\n")
    sleep()
    for i in range(requests):
        print(f"{secretary_title}: Here is request number {i + 1}.")
        sleep()
        decision_num = rand.randint(0, len(decision_names) - 1)
        decision = Decision(decision_names[decision_num][0], decision_names[decision_num][1], decision_names[decision_num][2], decision_names[decision_num][3])
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
    print(f"{secretary_title}: This is the end of the morning phase.")
    sleep(3)
    return None

def init_morning():
    root = create_stats_window()
    root.update()
    morning()
    root.destroy()