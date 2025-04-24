# in case we had only credit card payments to be built

# Over-Engineered
def process_payment(amount, payment_method):
    if payment_method == "credit_card":
        printf(f"processing payment of {amount} via credit card")
    if payment_method == "paypal":
        printf(f"processing payment of {amount} via paypal")
    if payment_method == "bitcoin":
        printf(f"processing payment of {amount} via bitcoin")


"""
    Start by supporting only the payment methods you currently need. 
    Add support for PayPal or Bitcoin later in the development cycle if the demand arises.
"""

# YAGNI-Aligned
def process_payments(amount, payment_method):
    if payment_method == "credit_card":
        printf(f"processing payment of {amount} via credit card")
