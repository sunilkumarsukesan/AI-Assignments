class BankAccount:

    def __init__(self, account_holder, balance, account_type):
        self.account_holder = account_holder
        self.balance = float(balance)
        self.account_type = account_type

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Amount deposited : {amount}")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Sorry insufficient balance")
        else:
            self.balance = self.balance - amount
            print (f"Dispensing cash : {amount}")

    def display_balance(self):
        print(f"Account Details:\n  Account Holder: {self.account_holder}\n  Type: {self.account_type}\n  Available Balance: {self.balance}\n")


if __name__ == "__main__":
    BankAccounts = [
        BankAccount("Sunil", 10000,"Savings"),
        BankAccount ("ABC", 20000, "Current")
    ]

    for BankAccount in BankAccounts :
        BankAccount.withdraw(20000)
        BankAccount.display_balance()
        BankAccount.withdraw(2000)
        BankAccount.display_balance()
        BankAccount.deposit(100)
        BankAccount.display_balance()
        print()
