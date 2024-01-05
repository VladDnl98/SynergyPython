a = (2, 4, 9, 7, 2)
print(a.count(2))

# Вывод большего и меньшего числа
# a = 5
# b = 8
# c = 1
# d = -19

# print(max(a, b, c, d))
# print(min(a, b, c, d))

# Сортировка 3 вариант
# def cmp(x):
#     return(x // 10) * (x % 10)

# tmp = [12, 34, 35, 12, 68, 29]
# tmp.sort(key=cmp)
# print(tmp)

# Сортировка по зарплате
# n = 5
# sph = [12, 30 , 97, 5 , 6]
# hs = [10, 120, 4, 8, 9]

# res = []

# for i in range(n):
#     r = sph[i] * hs[i]
#     res.append(r)

# res.sort()
# print(res)


# Обычная сортировка
# a = [1, 3, 6, 4, 5, 7, 2]

# a.sort()

# print(*a)

# Сортировка пузырьком
# a = [1, 3, 6, 4, 5, 7, 2]
# n = len(a)

# for i in range(n):
#     for j in range(n - 1 - i):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]

# print(*a)

# a = [1, 2, 3, 4, 5, 6 ,7 , 8]
# c1 = 3
# c2 = 4

# c1, c2 = c2, c1

# print(c1, c2)