import gamestate_tracking
from tutorial import tutorial
from morning import init_morning

def main():
    while True:
        if gamestate_tracking.phase == 0:
            tutorial()
        elif gamestate_tracking.phase == 1:
            init_morning()

if __name__ == "__main__":
    main()