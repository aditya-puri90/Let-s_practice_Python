'''Shopping Bill
Take:

Product price
Quantity

Calculate the total bill.'''

price = float(input("ENter the product price:"))
quantity = int(input("Enter the quantity you buy: "))

total_bill = price * quantity
print("Total bill =", total_bill)