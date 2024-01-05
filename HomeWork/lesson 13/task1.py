import random

# Создаем первую матрицу
matrix1 = [[random.randint(-50, 50) for _ in range(10)] for _ in range(10)]
print("Первая матрица:")
for row in matrix1:
    print(row)

# Создаем вторую матрицу
matrix2 = [[random.randint(-50, 50) for _ in range(10)] for _ in range(10)]
print("\nВторая матрица:")
for row in matrix2:
    print(row)

# Складываем матрицы и создаем третью матрицу
matrix3 = [[matrix1[i][j] + matrix2[i][j] for j in range(10)] for i in range(10)]
print("\nТретья матрица (сумма первой и второй):")
for row in matrix3:
    print(row)