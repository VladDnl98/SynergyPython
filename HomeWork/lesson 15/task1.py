class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return "Название автомобиля: " + self.name + " Скорость: " + str(self.max_speed) + " Пробег: " + str(self.mileage)


bus = Transport("Renault Logan", 180, 12)

print(bus)