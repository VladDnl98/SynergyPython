def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n

y=int(input())

for i in range(y,0,-1):
    print(fac(i))