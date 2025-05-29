import gamestate_tracking
from tutorial import sleep
from may_change import secretary_title

def evening():
    print(f"\n{secretary_title}: Good evening, {gamestate_tracking.player_name}.")
    sleep()
    print(f"{secretary_title}: {gamestate_tracking.newspaper_outlet} has sent over their newspaper for you to review.")