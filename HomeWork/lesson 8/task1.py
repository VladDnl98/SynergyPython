# Чтение значения N
N = int(input("Введите количество чисел: "))

# Инициализация списка для хранения чисел
numbers = []

# Чтение N чисел и добавление их в список
for i in range(N):
    num = int(input())
    numbers.append(num)

# Переворачивание списка
reversed_numbers = list(reversed(numbers))

# Вывод перевернутого массива
print("Перевернутый массив:", reversed_numbers)