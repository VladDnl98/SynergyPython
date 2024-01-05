class Human(object):
    name = "Ivan"
    height = 175
    age = 25

    def __init__(self, n, h, a):
        self.name = n
        self.height = h
        self.age = a

    def privet(self):
        print(f'My name is {self.name}, my age is {self.age}')

    
    def get_older(self):
        self.age += 5



h1 = Human('Anton', 120, 12)
h2 = Human('Dima', 190, 23)


h1.privet()
h1.get_older()
print(h1.age)
