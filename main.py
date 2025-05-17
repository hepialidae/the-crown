import gamestate_tracking
from tutorial import tutorial
from morning import morning
# from faction_stats import *

# root = create_stats_window()

def main():
    while True:
        print(f"Current phase: {gamestate_tracking.phase}")
        if gamestate_tracking.phase == 0:
            tutorial()
        elif gamestate_tracking.phase == 1:
            morning()

# root.mainloop()

if __name__ == "__main__":
    main()