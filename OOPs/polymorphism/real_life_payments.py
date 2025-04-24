"""
    real life example of payment system using polymorphic function

    When to use polymorphism in payment systems
        - Need to add a new payment system without modifying the existing ones
        - Provide a flexible and scalable design
        - Improves code readability and maintainability

"""
from abc import ABC, abstractmethod

class Payment:
    @abstractmethod
    def pay(self, amount):
        pass #abstract method, no implementation

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} via credit card using method {self.__class__.__name__}")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} via credit card using method {self.__class__.__name__}")

if __name__ == '__main__':
    payment_methods = [CreditCardPayment(), PayPalPayment()]
    for payment_method in payment_methods:
        payment_method.pay(100)
