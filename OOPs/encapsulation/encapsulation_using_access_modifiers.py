"""
    Python provides access modifiers to enforce encapsulation
    - public : accessible from anywhere
    - _protected : accessible in class and via subclass
    - __private: accessible only in the class

    Benefits -
    - does not provide unauthorized access to the data
    - allows controlled modifications through methods
"""

class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder # private attribute
        self.__balance = balance # private attribute using __ in the start

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount>0:
            self.__balance += amount
            print(f"Deposited {amount}")
        else:
            print("Invalid amount")

if __name__ == '__main__':
    bank_account = BankAccount("Adam", 1000)
    print(f"Current balance : {bank_account.get_balance()}")
    bank_account.deposit(100)
    print(f"Current balance : {bank_account.get_balance()}")
    bank_account.deposit(-5)
