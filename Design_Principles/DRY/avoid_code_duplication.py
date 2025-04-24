# instead of doing this

def calculate_food_tax(amount):
    return amount * 0.05

def calculate_clothing_tax(amount):
    return amount * 0.10

def calculate_electronics_tax(amount):
    return amount * 0.15

calculate_food_tax(10)
calculate_clothing_tax(20)
calculate_electronics_tax(30)

# do

def calculate_tax(amount, tax_rate):
    return amount * tax_rate

calculate_tax(10,0.05)
calculate_tax(20, 0.10)
calculate_tax(30, 0.15)