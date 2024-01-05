def pl(t):
    for i in t:
        print(*i)

t3 = [[[1, 2], [3, 4]], [[5,6], [7, 8]]]
print(t3[0][0][0])

# составление двумерно списка на примере этажей
# def pl(t):
#     for i in t:
#         print(*i)

# x = int(input("Введите количество этажей: "))
# y = int(input("Введите количество квартир: "))

# house = [[0 for i in range(y)] for i in range(x)]
# cnt = 1

# for i in range(-1, -x - 1, -1):
#     if i % 2 == 1:
#         for j in range(y):
#             house[i][j] = cnt
#             cnt += 1
#     else:
#         for j in range(-1, -y - 1, -1):
#             house[i][j] = cnt
#             cnt += 1


# pl(house)



# tmp = [[1 for i in range(3)] for i in range(5)]
# print(tmp)

# n = int(input("teax: "))
# tmp = []

# for i in range(n):
#     a = list(map(int, input().split()))
#     tmp.append(a)

# print(tmp)


# tmp = [[1, 2, 3], [4, 5], [9, 8, 7]]


# for i in tmp:
#     print(*i)