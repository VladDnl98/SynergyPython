from utils import randbool
from utils import randcell
from utils import randcell2

# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд шоп
# 5 - пожар

CELL_TYPES = "🟩🌲🌊🏥🏦🔥🟫"

THREE_BONUS = 100
UPGRADE_COST = 1000
LIVES_COST = 100
LIFE_COST = 1000
FIRE_COST = 1

class Map:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]
        self.generate_forest(5, 10)
        self.generate_river(10)
        self.generate_river(10)
        self.generate_upgrade_shop()
        self.generate_hospital()
        self.last_fire_updated_score = 0

    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True
    
    def print_map(self, helico, clouds):
        print("⬛️" * (self.w + 2))
        for ri in range(self.h):
            print("⬛️", end = "")
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if (clouds.cells[ri][ci] == 1):
                    print("🌩 ", end="")
                elif (clouds.cells[ri][ci] == 2):
                    print("🌪 ", end="")
                elif(helico.x == ri and helico.y == ci):
                    print("🚁", end="")
                elif (cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end="")
            print("⬛️")
        print("⬛️" * (self.w + 2))

    def generate_river(self, l):
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.check_bounds(rx2, ry2)):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1

    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    if self.cells[ri][ci] == 0:
                        self.cells[ri][ci] = 1
                    
                        

    def generate_tree(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1
        if (self.cells[cx][cy] == 6):
            self.cells[cx][cy] = 1

    def generate_upgrade_shop(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4

    def generate_hospital(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] != 4:
            self.cells[cx][cy] = 3
        else:
            self.generate_hospital()


    def add_fire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5
    
    def update_fires(self):
        w = self.w
        h = self.h
        new_cells = [[cell for cell in row] for row in self.cells]
        for ri in range(h):
            for ci in range(w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.last_fire_updated_score = FIRE_COST
                    new_cells[ri][ci] = 6
                elif cell == 1:
                    if ri - 1 >= 0 and self.cells[ri - 1][ci] == 5:
                        new_cells[ri][ci] = 5
                    if ri + 1 < h and self.cells[ri + 1][ci] == 5:
                        new_cells[ri][ci] = 5
                    if ci - 1 >= 0 and self.cells[ri][ci - 1] == 5:
                        new_cells[ri][ci] = 5
                    if ci + 1 < w and self.cells[ri][ci + 1] == 5:
                        new_cells[ri][ci] = 5
        self.cells = new_cells
        for i in range(5):
            self.add_fire()
    
    def process_helicopter(self, helico, clouds):
        c = self.cells[helico.x][helico.y]
        d = clouds.cells[helico.x][helico.y]
        helico.score -= self.last_fire_updated_score


        if c == 2:
            helico.tank = helico.mxtank
        elif c == 5 and helico.tank > 0:
            helico.tank -= 1
            helico.score += THREE_BONUS
            self.cells[helico.x][helico.y] = 1
        elif c == 4 and helico.score >= UPGRADE_COST:
            helico.mxtank += 1
            helico.score -= UPGRADE_COST
        elif c == 3 and helico.score >= LIFE_COST:
            helico.lives += LIVES_COST
            helico.score -= LIFE_COST
        if d == 2:
            helico.lives -= 1
        if helico.lives == 0:
            helico.game_over()
    
    
    

    def export_data(self):
        return {"cells": self.cells}
    
    def import_data(self, data):
        self.cells = data["cells"] or [[0 for i in range(self.w)] for j in range(self.h)]

