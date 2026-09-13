"""
Q21. Bank Account Getter/Setter with @property

Create a BankAccount class with:
    __balance
Create getter and setter functionality using @property.
The setter should not allow a negative balance.
"""


class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = None
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
            print(f"Balance updated to {amount}")
        else:
            print("Error: Balance cannot be negative!")

    def display_info(self):
        print(f"Account Holder: {self.account_holder}, Balance: {self.__balance}")


if __name__ == "__main__":
    acc1 = BankAccount("Aditya", 2000)
    acc1.display_info()

    acc1.balance = 3500
    acc1.balance = -500
    acc1.display_info()
