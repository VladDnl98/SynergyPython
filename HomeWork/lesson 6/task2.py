# Задание №2
# Вводится натуральное число X. Подсчитайте количество натуральных делителей числа X 
# (включая 1 и само число). x ≤ 2e9 (2 миллиарда)

#Вводим значение для переменной х
x = int(input("Введите число: "))
#назначение переменной count значение 0
count = 0
#Создаем цикл for который производит расчет, берет числа в диапозоне от 1 одного с шагом +1
#Добавляем условие если x остаток от деления i равен 0, тогда в переменную count добавляем 1 
for i in range(1, x+1):
    if x % i == 0:
        count += 1

print("Количество диелителей:", count)