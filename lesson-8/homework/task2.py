import json

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance if balance >=0 else 0
        
    def deposit(self, amount):
        if amount > 0:
             self.balance += amount
             return f"Deposited ${amount}. New balance: ${self.balance}"
        raise ValueError("Deposit must be positive")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdraw ${amount}. New balance: ${self.balance}"
        raise ValueError("Invalid withdrawal amount") 
        
class Bank(Account):
    def __init__(self):
        self.accounts = {}
        
    def create_account(self, account_number, name, initial_deposit):
        if account_number in self.accounts:
            return "Account number already exists."
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        return  f"Account for {name} created successfully"
    
    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return f"Account: {account.account_number}, Name: {account.name}, Balance: ${account.balance}"
        return "Account not found."

    def save_to_file(self, filename="accounts.json"):
        with open(filename, "w") as file:
            json.dump({acc: vars(self.accounts[acc]) for acc in self.accounts}, file)
        return "Accounts saved successfully."

    def load_from_file(self, filename="accounts.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.accounts = {acc: Account(**data[acc]) for acc in data}
            return "Accounts loaded successfully."
        except FileNotFoundError:
            return "No saved data found."

# Example usage:
bank = Bank()
print(bank.create_account(1001, "Alice", 500))
print(bank.create_account(1002, "Bob", 300))
print(bank.view_account(1001))
print(bank.accounts[1001].deposit(200))
print(bank.accounts[1001].withdraw(100))
print(bank.save_to_file())