import time
from may_change import *
import gamestate_tracking

def sleep(secs=1.2):
    time.sleep(secs)

def tutorial():
    global secretary_name, secretary_title
    print("Secretary: Welcome, Emanator!")
    sleep()
    print("Secretary: It's been a while since the Aether left. Now, it's up to you to rule.")
    sleep()
    new_name = input("Secretary: What shall you be known as? ")
    try:
        if new_name[0] != None:
            gamestate_tracking.player_name = new_name
    except IndexError:
        gamestate_tracking.player_name = gamestate_tracking.player_name
    sleep(0.3)
    print(f"{secretary_title}: Hello, {gamestate_tracking.player_name}. I am {secretary_name}. It is an honor to work as your secretary.\n")
    sleep()
    new_city = input(f"{secretary_title}: What do you want to name your city? ")
    try:
        if new_city[0] != None:
            new_city_words = new_city.split(" ")
            capitalized_city_words = []
            for word in new_city_words:
                capitalized_city_words.append(word.capitalize())
            gamestate_tracking.city_name = " ".join(capitalized_city_words)
    except IndexError:
        gamestate_tracking.city_name = gamestate_tracking.city_name
    print(f"{secretary_title}: {gamestate_tracking.city_name}, huh? Quite memorable, indeed.\n")
    sleep()
    print(f"{secretary_title}: This game has 3 phases: Morning, Afternoon, and Night.")
    sleep()
    decided = False
    while decided == False:
        tutorial_decision = input(f"{secretary_title}: Would you like me to explain them? Enter 'Yes' if you do, and 'No' if not. ")
        if tutorial_decision.lower() == "no":
            decided = True
            print("\n")
            sleep(0.3)
            gamestate_tracking.phase = 1
            return None
        elif tutorial_decision.lower() == "yes":
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
    print(f"{secretary_title}: At Night, you will be shown the newspaper stories that will be released tomorrow.")
    sleep()
    print(f"{secretary_title}: You can choose to edit or delete existing stories, and add new ones.\n")
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
    gamestate_tracking.phase = 1
    print("\n")
    return None