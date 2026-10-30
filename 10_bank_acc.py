# 10 Bank Account 

class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Current Balance:", self.balance)
        else:
            print("Insufficient balance!")

    def display(self):
        print("\nAccount Details")
        print("Account Number:", self.acc_no)
        print("Account Holder:", self.name)
        print("Account Type:", self.acc_type)
        print("Current Balance:", self.balance)

acc_no = input("Enter account number: ")
name = input("Enter account holder name: ")
acc_type = input("Enter account type: ")
balance = int(input("Enter initial balance: "))

account = BankAccount(acc_no, name, acc_type, balance)
deposit_amount = int(input("Enter amount to deposit: "))
account.deposit(deposit_amount)
withdraw_amt = int(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amt)
account.display()