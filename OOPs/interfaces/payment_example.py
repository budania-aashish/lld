from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass


class PhonePe(Payment):
    def make_payment(self, amount):
        print(f"{amount} paid via phonepe")

class Paytm(Payment):
    def make_payment(self, amount):
        print(f"{amount} paid via paytm")


if __name__ == "__main__":
    phone_pe = PhonePe()
    phone_pe.make_payment(100)
    paytm = Paytm()
    paytm.make_payment(101)
