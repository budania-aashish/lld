"""
    prevents direct modification of the important fields
    Ensures data integrity by validating inputs 
"""

class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance

    def validate_withdraw(self, amount):
        if amount >= self.__balance:
            return False
        return True

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if self.validate_withdraw(amount):
            self.__balance-=amount
            print(f"Withdraw successful for {amount}")
        else:
            print(f"Amount to withdraw is greater than balance {self.__balance}")

if __name__ == '__main__':
    bank_account = BankAccount("Adam", 100)
    bank_account.withdraw(101)
    print(f"Balance in the bank account is {bank_account.get_balance()}")
    bank_account.withdraw(50)
    print(f"Balance in the bank account is {bank_account.get_balance()}")


