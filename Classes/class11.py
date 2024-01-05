def new_year():
    print("Happy New Year!")

def birthday():
    name = input("Tell us name of a person")
    print(f"Happy birhday, {name}!")

def mart8():
    print("Happy 8th March!")

n = int(input())

for i in range(n):
    cm = input()
    if cm == 'new year':
        new_year
    elif cm == 'birtday':
        birthday()
    elif cm == '8 march':
        mart8()
    else:
        print("wrong command")



# def nechet(n):
#     return (n % 2 != 0)

# def res(l):
#     for el in l:
#         if nechet(el):
#             print(el)

# tmp = [1 , 2, 3, 4, 5, 6]
# res(tmp)


# def vis(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     return False

# y = int(input())
# print(vis(y))


# def tmp(name):
#     print(f"hello, {name}")

# tmp('Mark')