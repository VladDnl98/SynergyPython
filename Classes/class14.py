import sys

def tmp(n):
    if n < 0:
        return
    print(n)
    tmp(n - 1)

sys.setrecursionlimit(1000)
tmp(500)


# Рекурсия
# def fib(n):
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     res = fib(n-1) + fib(n - 2)
#     return res

# x = 5

# print(fib(x))

# def tmp(x):
#     if x < 0:
#         return
#     tmp(x-1)
#     print(x)

# n = int(input())
# tmp(n)


# def tmp(x):
#     if x < 0:
#         return
#     print(x)
#     tmp(x-1)

# n = int(input())
# tmp(n)

# def test(a, b, c):
#     return a + b + c

# d = test(3, 4, 9)
# print(d)