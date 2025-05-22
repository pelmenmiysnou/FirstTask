#1
class BankAccount:
    def __init__(self):
        self._balance = 0  
    
    @property
    def balance(self):
        return self._balance
    

    def set_balance(self, value):
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self._balance = value
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += amount
        return self._balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self._balance:
            raise ValueError(f"Недостаточно средств. Доступно: {self._balance}")
        self._balance -= amount
        return self._balance

    def __str__(self):
        return f"Банковский счет с балансом: {self._balance} руб."

account = BankAccount()
print(account)  

try:
    account.deposit(1000)
    print(account)  
    
    account.withdraw(500)
    print(account)  
    
    account.withdraw(1000)
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    account.set_balance(-100)
except ValueError as e:
    print(f"Ошибка: {e}")

print(account)

