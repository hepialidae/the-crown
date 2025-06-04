import gamestate_tracking

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
    print("   0   1   2   3   4")
    for row in range(len(gamestate_tracking.city_grounds)):
        row_display = [f"{row} "]
        texts = []
        for column in range(len(gamestate_tracking.city_grounds[row])):
            if column == 0:
                texts.append(f"[{gamestate_tracking.city_grounds[row][column].text}")
            elif column == len(gamestate_tracking.city_grounds[row]) - 1:
                texts.append(f"{gamestate_tracking.city_grounds[row][column].text}]")
            else:
                texts.append(f"{gamestate_tracking.city_grounds[row][column].text}")
        grids = "] [".join(texts)
        row_display.append(grids)
        print(f"{''.join(row_display)}")