class BankAccount:
    def __init__(self, account_number, balance, account_type):
        # TODO: Set instance variables for each value
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        # TODO: Add the specified amount to the account balance
        self.balance += amount
        
    def withdraw(self, amount):
        # TODO: Subtract the specified amount from the account balance
        self.balance -= amount

    def display_balance(self):
        # TODO: Print out the current balance of the account
        print(self.balance)

# TODO: Create a BankAccount object
BankAccount_1 = BankAccount("23498293234", 0, "savings")

# TODO: Call the deposit and withdraw methods on the account object
BankAccount_1.deposit(100)

BankAccount_1.withdraw(50)

# TODO: Call the display_balance method on the account object to make sure it's working correctly
BankAccount_1.display_balance()
