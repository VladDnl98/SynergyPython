import random

# Ввод размеров матрицы
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Создаем первую матрицу
matrix1 = [[random.randint(-50, 50) for _ in range(cols)] for _ in range(rows)]
print("Первая матрица:")
for row in matrix1:
    print(row)

# Создаем вторую матрицу
matrix2 = [[random.randint(-50, 50) for _ in range(cols)] for _ in range(rows)]
print("\nВторая матрица:")
for row in matrix2:
    print(row)

# Складываем матрицы и создаем третью матрицу
matrix3 = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
print("\nТретья матрица (сумма первой и второй):")
for row in matrix3:
    print(row)