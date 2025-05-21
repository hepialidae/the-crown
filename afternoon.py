from factions import *
from building import *
from may_change import *
import gamestate_tracking
from tutorial import sleep

def afternoon():
    gamestate_tracking.treasury["currency"] += tax_per_day
    print(f"\n{secretary_title}: Good afternoon, {gamestate_tracking.player_name}.")
    sleep(0.8)
    print(f"{secretary_title}: You may develop the city using the resources you have.")
    sleep()
    print(f"{secretary_title}: You have {gamestate_tracking.treasury['currency']} coins.")
    sleep()
    choice = None
    while choice != "exit":
        print(f"\n{secretary_title}: Enter '1' to build a building.")
        sleep(0.5)
        print(f"{secretary_title}: Enter '2' to interact with a building on the grid.")
        sleep(0.5)
        print(f"{secretary_title}: Enter '3' to check your treasury.")
        sleep(0.5)
        print(f"{secretary_title}: Enter '4' to view your city.")
        sleep(0.5)
        print(f"{secretary_title}: Enter 'Exit' to exit this phase.")
        sleep(0.5)
        choice = input(f"{secretary_title}: What would you like to do? ").lower().strip()
        if choice == "1":
            print(f"\n{secretary_title}: Here's what your city looks like:\n")
            show_city_grounds()
            sleep()
            buildable = find_buildable_buildings()
            print(f"\n{secretary_title}: You can build the following buildings: {buildable}.")
            lower_buildable = buildable.lower()
            building_choice = None
            while building_choice == None or building_choice not in lower_buildable:
                building_choice = input(f"{secretary_title}: Which building would you like to build? ").lower().strip()
                if building_choice not in lower_buildable:
                    print(f"\n{secretary_title}: You can only build the following buildings: {buildable}.")
                    sleep()
            appropriate_choice = False
            while appropriate_choice == False:
                print(f"\n{secretary_title}: Where would you like to build the new building?")
                sleep(0.5)
                position_choice = input(f"{secretary_title}: Enter the coordinates in the format 'row, column': ").strip()
                try:
                    coords = list(map(int, position_choice.split(", ")))
                    row = coords[0]
                    column = coords[1]
                    if gamestate_tracking.city_grounds[row][column].building != None:
                        print(f"\n{secretary_title}: There is already a building there.")
                        sleep()
                        appropriate_choice = False
                    else:
                        building_dict[building_choice].build(row, column)
                        appropriate_choice = True
                        print(f"\n{secretary_title} Here's what your city looks like now:")
                        show_city_grounds()
                        sleep()
                except ValueError:
                    print(f"\n{secretary_title}: Please make sure the coordinates entered are in the right format.")
                    sleep(0.5)
        elif choice == "2":
            appropriate_interaction_choice = False
            while appropriate_interaction_choice == False:
                print(f"\n{secretary_title}: Which grid would you like to interact with?")
                sleep(0.5)
                grid_choice = input(f"{secretary_title}: Enter the coordinates in the format 'row, column': ").strip()
                try:
                    coords = list(map(int, grid_choice.split(", ")))
                    row = coords[0]
                    column = coords[1]
                    if gamestate_tracking.city_grounds[row][column].building == None:
                        print(f"\n{secretary_title}: There is no building there to interact with.")
                        sleep()
                    else:
                        interact_building = gamestate_tracking.city_grounds[row][column].building
                        print(f"\n{secretary_title}: The building there is the {interact_building.name}.")
                        sleep()
                        print(f"{secretary_title}: You can interact with this building in the following ways:")
                        building_interactions = interact_building.interactions
                        if building_interactions == None:
                            print(f"\n{secretary_title}: There are no interactions for that building.")
                            appropriate_interaction_choice = True
                            break
                        else:
                            for i in range(len(building_interactions)):
                                print(f"{i + 1}. {building_interactions[i]}")
                            while True:
                                interact_choice = input(f"\n{secretary_title}: Enter the number corresponding to the interaction: ").lower().strip()
                                if interact_choice == "1":
                                    interact_building.interaction1()
                                    appropriate_interaction_choice = True
                                    break
                                elif interact_choice == "2":
                                    interact_building.interaction2()
                                    appropriate_interaction_choice = True
                                    break
                                elif interact_choice == "exit":
                                    appropriate_interaction_choice = True
                                    break
                                else:
                                    print(f"\n{secretary_title}: Please enter an appropriate number or 'exit'.")
                except ValueError:
                    print(f"\n{secretary_title}: Please make sure the coordinates entered are in the right format.")
                    sleep(0.5)
        elif choice == "3":
            print(f"\n{secretary_title}: You have {gamestate_tracking.treasury['currency']} coins.")
            sleep()
        elif choice == "4":
            print(f"\n{secretary_title}: Here's what your city looks like:\n")
            show_city_grounds()
            sleep()
    sleep()
    gamestate_tracking.phase = 3
    return None