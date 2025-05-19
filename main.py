import sys
from grid import *
from building import *
from factions import *
from may_change import *
import gamestate_tracking
from tutorial import tutorial
from morning import init_morning
from endings import check_endings

def main():
    # core gameplay loop
    while True:
        if gamestate_tracking.phase == 0:
            tutorial()
        elif gamestate_tracking.phase == 1:
            init_morning()
            check_endings()
        elif gamestate_tracking.phase == 2:
            pass # not implemented yet
        elif gamestate_tracking.phase == 3:
            pass # not implemented yet
        elif gamestate_tracking.phase == 4:
            sys.exit()

if __name__ == "__main__":
    main()