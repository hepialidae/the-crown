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
        try:
            decision = Decision(decision_names[decision_num][0], decision_names[decision_num][1], decision_names[decision_num][2], decision_names[decision_num][3], decision_names[decision_num][4], decision_names[decision_num][5])
        except IndexError:
            decision = Decision(decision_names[decision_num][0], decision_names[decision_num][1], decision_names[decision_num][2], decision_names[decision_num][3], decision_names[decision_num][4])
        print(f"{secretary_title}: {decision.text}")
        sleep()

        # consult with advisors
        appropriate_advice_choice = False
        while appropriate_advice_choice == False:
            print(f"\n{secretary_title}: Before you make your decision, you are free to consult with the advisors.")
            sleep()
            print(f"{secretary_title}: Enter '1' to consult the {advisor_names[0]}. (The Arcanum)")
            sleep(0.3)
            print(f"{secretary_title}: Enter '2' to consult the {advisor_names[1]}. (The Commoners)")
            sleep(0.3)
            print(f"{secretary_title}: Enter '3' to consult the {advisor_names[2]}. (The Gilded)")
            sleep(0.3)
            print(f"{secretary_title}: Enter '4' to consult the {advisor_names[3]}. (The Iron Guard)")
            sleep(0.3)
            print(f"{secretary_title}: Enter '5' to consult the {advisor_names[4]}. (The Veiled)")
            sleep(0.3)
            print(f"{secretary_title}: Enter 'decided' to move on to making your decision.")
            sleep(0.3)
            advisor_choice = input(f"{secretary_title}: What would you like to do? ").strip()
            if advisor_choice in "12345":
                int_advisor_choice = int(advisor_choice) - 1
                decision.discuss_with_advisor(advisor_names[int_advisor_choice])
                appropriate_advice_choice = False # player can discuss with more than one advisor
            elif advisor_choice.lower() == "decided":
                print(f"{secretary_title}: Very well. Let's move on.\n")
                appropriate_advice_choice = True
            else:
                print(f"\n{secretary_title}: Please enter a number from 1-5 or 'decided'.")
                sleep(0.5)
                appropriate_advice_choice = False
        
        # make your decision
        appropriate_decision_choice = False
        while appropriate_decision_choice == False:
            print(f"{secretary_title}: {decision.text}")
            sleep()
            choice = input(f"{secretary_title}: Enter A or B to make your choice: ")
            if choice.lower() == "a":
                decision.option_1()
                appropriate_decision_choice = True
            elif choice.lower() == "b":
                decision.option_2()
                appropriate_decision_choice = True
            else:
                print(f"\n{secretary_title}: Invalid choice. Please enter A or B.\n")
                sleep(0.5)
        show_faction_stats()
    print(f"{secretary_title}: This is the end of the morning phase.")
    gamestate_tracking.phase = 2
    sleep(3)
    return None

morning()