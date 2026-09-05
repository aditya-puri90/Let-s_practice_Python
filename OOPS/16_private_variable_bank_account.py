'''
Q16. Private variable

Create a BankAccount class with a private variable:

__balance

Create methods:

deposit()
withdraw()
get_balance()

Try accessing __balance directly and observe what happens.
'''

class BankAccount:

    def __init__(self,account_holder,_balance = 0):

        self.account_holder = account_holder
        self._balance = _balance

    def deposit(self,amount):
        self._balance+= amount
        print(f"Deposited Amount:{amount}, new balance :{self._balance}")

    def withdraw(self,amount):
        if amount<=self._balance:
            self._balance-=amount
            print(f"Withdraw:{amount},New balance:{self._balance}")
        else:
            print("Insufficient balance ! Withdraw cancelled")

    def get_balance(self,amount):

            return self._balance

acc1 = BankAccount("Aditya",2000000)
print("initial balance:", acc1.get_balance)

acc1.deposit(500)
acc1.withdraw(300)

print(acc1._balance)