def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def get_factorial_list(number):
    fact = factorial(number)
    result = [factorial(i) for i in range(1, min(number+5, number+1))]
    result.reverse()
    return result

# Пример использования
input_number = int(input("Введите число: "))
result_factorial = factorial(input_number)
result_list = get_factorial_list(result_factorial)

print("Факториал числа", input_number, ":", result_factorial)
print("Результирующий список факториалов:", result_list)