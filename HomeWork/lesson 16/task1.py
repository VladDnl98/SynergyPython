class Cassa:
    def __init__(self, initial_amount):
        self.balance = initial_amount

    def top_up(self, amount):
        self.balance += amount

    def count_1000(self):
        thousand_notes = self.balance // 1000
        return thousand_notes

    def take_away(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Not enough money in the cash register")

# Пример использования класса
cash_register = Cassa(5000)
print("Текущий баланс в кассе:", cash_register.balance)

cash_register.top_up(3000)
print("Текущий баланс в кассе после пополнения на 3000:", cash_register.balance)
print("Целых тысяч в кассе:", cash_register.count_1000())