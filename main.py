import sys
import gamestate_tracking
from evening import evening
from tutorial import tutorial
from afternoon import afternoon
from morning import morning
from endings import check_endings

def main():
    # core gameplay loop
    while True:
        if gamestate_tracking.phase == 0:
            tutorial()
        elif gamestate_tracking.phase == 1:
            morning()
            check_endings()
        elif gamestate_tracking.phase == 2:
            afternoon()
            check_endings()
        elif gamestate_tracking.phase == 3:
            evening()
        elif gamestate_tracking.phase == 4:
            sys.exit()

if __name__ == "__main__":
    main()