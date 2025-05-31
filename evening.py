import gamestate_tracking
from tutorial import sleep
from newspaper import Newspaper
from may_change import secretary_title

def evening():
    # newspaper stuff
    gamestate_tracking.todays_newspaper.add_silly_article()
    
    print(f"\n{secretary_title}: Good evening, {gamestate_tracking.player_name}.")
    sleep()
    print(f"{secretary_title}: {gamestate_tracking.newspaper_outlet} has sent over their newspaper for you to review.")
    sleep()
    gamestate_tracking.todays_newspaper.print_newspaper()
    choice = ""
    while choice.lower() != "exit" or choice.lower() != "q":
        print(f"{secretary_title}: Enter '1' to delete an article.")
        print(f"{secretary_title}: Enter 'exit' to exit this phase.")
        choice = input(f"{secretary_title}: What would you like to do? ")
        if choice == "1":
            appropriate = False
            while appropriate == False:
                gamestate_tracking.todays_newspaper.print_newspaper()
                try:
                    article = int(input(f"{secretary_title}: Which article would you like to delete? Enter the number here: "))
                    appropriate = True
                except ValueError:
                    print(f"{secretary_title}: Please enter a valid article number.")
                    sleep()
                    appropriate = False
            gamestate_tracking.todays_newspaper.delete_article(article - 1)
            sleep(0.3)
            print(f"{secretary_title}: Alright, I'll tell them to delete that article.")

    gamestate_tracking.phase = 1
    print("\n")
    sleep(3)
    return None

evening()