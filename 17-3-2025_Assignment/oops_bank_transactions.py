""" Steps: 
1. Define a custom exception InsufficientFundsError to handle withdrawal errors. 
2. Create a class BankAccount with:  
o A balance attribute initialized to 0. 
o A method deposit(amount):  
▪ Raise ValueError if amount <= 0. 
▪ Add the amount to balance. 
o A method withdraw(amount):  
▪ Raise InsufficientFundsError if amount > balance. 
▪ Deduct the amount from balance. 
3. Implement exception handling while performing transactions. 
Example: 
account = BankAccount() 
account.deposit(100) 
account.withdraw(150)  # Should raise InsufficientFundsError """


#code:

class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds in account"):
        super().__init__(message)

# Step 2: Create a BankAccount class
class BankAccount:
    def __init__(self):
        self.balance = 0  # Initialize balance to 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Withdrawal amount exceeds account balance.")
        self.balance -= amount

# Step 3: Exception handling while performing transactions
try:
    account = BankAccount()
    account.deposit(100)
    account.withdraw(70) 
    print(account.balance)
  
except ValueError as ve:
    print(f"ValueError: {ve}")
except InsufficientFundsError as ife:
    print(f"InsufficientFundsError: {ife}")