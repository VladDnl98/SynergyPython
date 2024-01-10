def invest_decision(min_investment, michael_money, ivan_money):
    if michael_money >= min_investment and ivan_money >= min_investment:
        return 2
    elif michael_money >= min_investment:
        return 1
    elif ivan_money >= min_investment:
        return 1
    elif michael_money + ivan_money >= min_investment:
        return 1
    else:
        return 0

X = int(input("Введите минимальную сумму инвестиций: "))
A = int(input("Сколько денег у Майкла? "))
B = int(input("Сколько денег у Ивана? "))

result = invest_decision(X, A, B)
print("Результат:", result)