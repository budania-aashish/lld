"""

    Banking Systems: Ensuring account details are private
    Healthcare Applications: Protecting patient records
    E-Commerce: Hiding payment processing details

    Benefits
    - protects sensitive data like card number
    - hides unnecessary details from users
    - ensures secure transactions

"""

class PaymentProcessor:
    def __init__(self, card_number, amount):
        self.__card_number = self.__mask_card_number(card_number)
        self.__amount = amount

    # the __mask_car_number function is private, can't be accessed from outside
    def __mask_card_number(self, card_number):
        return "****-****-****-" + card_number[-4:]

    def process_payment(self):
        print(f"Processing payment of {self.__amount} using card number {self.__card_number}")


if __name__ == '__main__':
    payment_processor = PaymentProcessor("4532875913527687", 250)
    payment_processor.process_payment()
    # payment_processor.__mask_car_number("8684757832874321") - error because we can't access private method

