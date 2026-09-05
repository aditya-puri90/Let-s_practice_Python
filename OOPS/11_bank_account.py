'''
Q11. Bank Account

Create a BankAccount class with:

account_holder
balance

Create methods:

deposit()
withdraw()
check_balance()

Make sure withdrawal doesn't happen if the balance is insufficient.

'''

class BankAccount:

    def __init__(self,account_holder,balance=0):

        self.account_holder = account_holder
        self.balance = balance

    def deposite(self,amount):
        self.balance += amount

        print(f"Deposited amount {amount}. New balance {self.balance}")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance -= amount
            print(f"Withdraw amount:{amount}. New balance {self.balance}")
        else:
            print("Insufficient balance")

    def check_balance(self):

        print(f"Account Holder:{self.account_holder}.Balance :{self.balance}")


acc1 = BankAccount("Ram", 1000)

acc1.check_balance()
acc1.deposite(500)

acc1.withdraw(300)
acc1.withdraw(1500)






