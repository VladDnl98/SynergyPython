import random 
import math 
 
class Turtle: 
    def __init__(self, x, y, s): 
        self.x = x 
        self.y = y 
        self.s = s 
 
    def go_up(self): 
        self.y += self.s 
 
    def go_down(self): 
        self.y -= self.s 
 
    def go_left(self): 
        self.x -= self.s 
 
    def go_right(self): 
        self.x += self.s 
 
    def evolve(self): 
        self.s = min(self.s + 1, 5) 
 
    def degrade(self): 
        if self.s <= 1: 
            raise ValueError("s не может быть ≤ 0") 
        else: 
            self.s -= 1 
 
    def count_moves(self, x2, y2): 
        dx = abs(x2 - self.x) 
        dy = abs(y2 - self.y) 
        return math.ceil(dx / self.s) + math.ceil(dy / self.s) 
 
 
turtle = Turtle(random.randint(0, 800), random.randint(0, 600), random.randint(1, 5)) 
 
dest_x = random.randint(0, 800) 
dest_y = random.randint(0, 600) 
 
min_moves = turtle.count_moves(dest_x, dest_y) 
print(f"Минимальное количество ходов: {min_moves}")