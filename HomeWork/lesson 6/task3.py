# #Задание №3
# Вводятся целые числа A и B. Гарантируется, что A ≤ B. 
# Выведите все четные числа на заданном отрезке через пробел.

#Создаем переменные с вводом A и B
a=int(input("Введите первое число А: "))
b=int(input("Введите второе число В: "))

#Создаем цикл for
for i in range(a, b + 1):
    if i % 2 == 0:
        #Выводим полученный результат в одну строку через пробел
        print(i, end=' ')