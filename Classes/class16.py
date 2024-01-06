class Car(object):
    brand = 'Mazda'
    color = 'black'
    max_speed = 100
    __password = 1234


    def __init__(self, b, ms):
        self.brand = b
        self.max_speed = ms

    def __updade_password(self):
        self.__password = 234

    def upgrade(self):
        self.__updade_password += 25

    def get_password(self):
        return self.__password
    

tmp = Car('mazda', 3)
print(tmp.get_password())
tmp.__updade_password()
print(tmp.get_password())

# tmp = Car('lada', 2)
# tmp.disk_size = 45

# print(tmp.disk_size)

# class Truck(Car):
#     max_weight = 10

#     def __init__(self, b, ms, mw):
#         super().__init__(b, ms)
#         self.max_weight = mw

#     def add(self):
#         self.max_weight += 10

# gazel = Truck('Gazel', 60)
# gazel.upgrade()
# gazel.add()
# print(gazel.max_speed, gazel.max_weight)

# nissan = Car('Nissan', 190)
# print(nissan.brand, nissan.max_speed)