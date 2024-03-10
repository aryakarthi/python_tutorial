class BankAccount:

    count = 0

    # Constructor to initialize the bank account
    def __init__(self, account_number, account_holder, branch, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.branch = branch
        BankAccount.count += 1

    @property
    def greet(self):
        return f"Hello {self.account_holder}!"

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit {amount} successful. New balance: {self.balance}"
        else:
            return "Invalid deposit amount."

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal {amount} successful. Remaining balance: {self.balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    # Method to display account details
    def display_account_details(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: {self.balance}\nBranch: {self.branch}"

    # class method decorator
    @classmethod
    def showcount(cls):
        return cls.count

    # static method
    @staticmethod
    def msg():
        return "Thank you!"


# Creating an instance of the BankAccount class
account1 = BankAccount('12345678', 'Peter Parker', "Newyork", 1000)

# property decorator - access method like attribute
print(account1.greet)

# Displaying account details
print(account1.display_account_details())

# Depositing money
print(account1.deposit(500))

# Withdrawing money
print(account1.withdraw(200))

# Displaying balance details
print(f"Current Balance : {account1.balance}")

# Calling static method
print(account1.msg())

# Creating another instance of the BankAccount
account2 = BankAccount('56781234', 'Tony Stark', "Los Vegas", 5000)
print(account2.greet)
print(account2.display_account_details())
print(account2.msg())


# Calling class method
print(f"No of accounts : {BankAccount.showcount()}")
