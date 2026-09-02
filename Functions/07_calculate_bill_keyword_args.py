"""
Q7. Keyword Arguments

Create calculate_bill(price, quantity)
Call the function using keyword arguments and return the total bill.
"""

def calculate_bill(price, quantity):
    return price * quantity

total = calculate_bill(price=500, quantity=3)
print("Total Bill:", total)
