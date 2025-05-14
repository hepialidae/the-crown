from factions import *
from gamestate_tracking import *
from tutorial import *

def main():
    global phase
    if phase == "tutorial":
        init_factions()
        show_faction_stats()

if __name__ == "__main__":
    main()