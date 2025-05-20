import gamestate_tracking
import factions

class Grid():
    def __init__(self, row, column, building=None):
        self.row = row
        self.column = column
        self.position = (row, column)
        self.building = building
        if building is None:
            self.text = "o"
        else:
            self.text = "x"
    
    # only Building.build() should call this
    def hold_building(self, building):
        self.building = building
        self.text = "x"

# initializes grid to make it not empty space, and instead a grid filled with Grid objects
for row in range(len(gamestate_tracking.city_grounds)):
    for column in range(len(gamestate_tracking.city_grounds[row])):
        gamestate_tracking.city_grounds[row][column] = Grid(row, column)

def show_city_grounds():
    for row in gamestate_tracking.city_grounds:
        row_display = []
        for i in range(len(row)):
            if i == 0:
                row_display.append(f"[{row[i].text}")
            elif i == len(row) - 1:
                row_display.append(f"{row[i].text}]")
            else:
                row_display.append(f"{row[i].text}")
        print("], [".join(row_display))