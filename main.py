from factions import *

def init_factions():
    global faction_list
    names = ["The Arcanum", "The Veiled", "The Gilded", "The Commoners"]
    for name in names:
        faction_list.append(Faction(name))
    faction_list.append(Iron_Guard())

def show_faction_stats():
    global faction_list
    for faction in faction_list:
        print(f"{faction.name}:")
        if faction.name == "The Iron Guard":
            print(f"Military Presence: {faction.presence}")
        else:
            print(f"Favor: {faction.favor}")
        print(f"Suspicion: {faction.suspicion}\n")

def main():
    pass

if __name__ == "__main__":
    main()