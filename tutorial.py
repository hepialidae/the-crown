from gamestate_tracking import *
import time
from names import *

def sleep(secs=1.0):
    time.sleep(secs)

def tutorial():
    global player_name, secretary_name
    print("Welcome, Emanator!")
    sleep()
    print("It's been a while since the Aether left. Now, it's up to you to rule.")
    sleep()
    new_name = input("What shall you be known as? ")
    if new_name != None or player_name != "":
        player_name = new_name
    sleep(0.3)
    print(f"Hello, {player_name}. I am {secretary_name}. It is an honor to work as your secretary.")