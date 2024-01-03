# Введите пятизначное целое число
number = int(input("Введите пятизначное целое число: "))

# Извлечение единиц, десятков, сотен, тысяч и десятков тысяч
units = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
ten_thousands = (number // 10000) % 10

# Возведение количества десятков в степень количества единиц
tens_power_units = tens ** units

# Умножение результат на количество сотен
result = tens_power_units * hundreds

# Деление полученного числа на разность количества десятков тысяч и количества тысяч
result /= (ten_thousands - thousands)

# Вывод результата
print("Результат:", result)