class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.balance}")

    def check_balance(self):
        print(f"Account Balance: {self.balance}")



class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, account_number):
        if account_number in self.accounts:
            print("Account already exists!")
        else:
            account = BankAccount(name, account_number)     #creates a BankAccount object
            self.accounts[account_number] = account         #stores that object inside the Bank
            print("Account created successfully!")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)


bank = Bank()

# Create accounts
bank.create_account("SadiK", 1001)
bank.create_account("Raj", 1002)
bank.create_account("Nayeem", 1003)

# Access account
account = bank.get_account(1001)

# Perform operations
if account:
    account.deposit(500)
    account.withdraw(200)
    account.check_balance()