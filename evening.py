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

    gamestate_tracking.phase = 1
    print("\n")
    sleep(3)
    return None