from factions import *
from gamestate_tracking import *
from tutorial import *

def main():
    global phase
    if phase == 0:
        tutorial()

if __name__ == "__main__":
    main()