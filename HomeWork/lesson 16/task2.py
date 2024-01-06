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
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError("S cannot be decreased further")

    def count_moves(self, x2, y2):
        x_diff = abs(self.x - x2)
        y_diff = abs(self.y - y2)
        return x_diff + y_diff

# Пример использования класса
t = Turtle(0, 0, 3)
t.go_up()
t.go_right()
t.evolve()
print(t.x, t.y, t.s)

try:
    t.degrade()
except ValueError as e:
    print(e)

moves = t.count_moves(3, 3)
print("Минимальное количество действий:", moves)