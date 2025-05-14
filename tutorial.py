from gamestate_tracking import *
import time
from names import *

def sleep(secs=1.2):
    time.sleep(secs)

def tutorial():
    global player_name, secretary_name, phase
    print("Secretary: Welcome, Emanator!")
    sleep()
    print("Secretary: It's been a while since the Aether left. Now, it's up to you to rule.")
    sleep()
    new_name = input("Secretary: What shall you be known as? ")
    try:
        if new_name[0] != None:
            player_name = new_name
    except IndexError:
        player_name = player_name
    sleep(0.3)
    print(f"{secretary_title}: Hello, {player_name}. I am {secretary_name}. It is an honor to work as your secretary.\n")
    sleep()
    print(f"{secretary_title}: This game has 3 phases: Morning, Afternoon, and Night.")
    sleep()
    decided = False
    while decided == False:
        tutorial_decision = input(f"{secretary_title}: Would you like me to explain them? Enter 'Yes' if you do, and 'No' if not. ")
        if tutorial_decision == "No" or tutorial_decision == "no":
            decided = True
            print("\n")
            sleep(0.3)
            phase = 1
            return None
        elif tutorial_decision == "Yes" or tutorial_decision == "yes":
            decided = True # then moves on to what's below the while loop
        else:
            decided = False
            print(f"{secretary_title}: Please enter 'Yes' or 'No'.")
    sleep(0.3)
    print(f"\n{secretary_title}: Sure! In the Morning, you make decisions and make policies.")
    sleep()
    print(f"{secretary_title}: Some decisions have immediate consequences, while others have to be implemented.")
    sleep()
    print(f"{secretary_title}: You implement policies in the Afternoon phase, when you can build.")
    sleep()
    print(f"{secretary_title}: At Night, you can go to the tavern to see what people think of you.\n")
    sleep(5)
    print(f"\n{secretary_title}: This game has 5 factions, each representing a different element.")
    sleep()
    print(f"{secretary_title}: To be a good ruler, you should balance the favor and suspicion of each faction.")
    sleep(5)
    print(f"{secretary_title}: Well, it seems our time is up.")
    sleep()
    print(f"{secretary_title}: It's time for you to rule!")
    sleep()
    input(f"{secretary_title}: Press any button when you're ready to proceed.")
    sleep()
    phase = 1
    print("\n")
    return None