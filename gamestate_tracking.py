day = 1
phase = 0 # 0 = tutorial; 1 = morning; 2 = afternoon; 3 = night; 4 = end
player_name = "Your Eminence"
treasury = {
    "currency": 0
}

# THIS IS A GRID. USING THE COORD SYSTEM. (0, 0) is the top left corner, while (4, 4) is the bottom right corner.
# The first index is the y-coordinate, while the second index is the left coordinate.
# x represents a building, while " " represents empty space.
# At the beginning of the game, (2, 2) contains the palace.
city_grounds = [
    [[" "], [" "], [" "], [" "], [" "]], 
    [[" "], [" "], [" "], [" "], [" "]], 
    [[" "], [" "], ["x"], [" "], [" "]], 
    [[" "], [" "], [" "], [" "], [" "]], 
    [[" "], [" "], [" "], [" "], [" "]]
    ]

#      0      1      2      3     4
#  0
#  1
#  2
#  3
#  4
