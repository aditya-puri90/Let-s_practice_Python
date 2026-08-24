'''Take:

Product name
Price
Quantity

Calculate the total price.

Output:

========== BILL ==========
Product: Laptop
Price: ₹50000
Quantity: 2
Total: ₹100000
==========================

Use escape sequences to make it look like a proper bill.'''

p_name= str(input("Enter the Product name:"))
Price= int(input("Enter the product price:"))
Quantity= int(input("Enter the Quantity:"))

print("\n ======BILL======")
print("\t Product Name:", p_name)
print("\t Price :", Price)
print("\t Quantity :", Quantity)
print("\t Total Bill :",Price*Quantity)
print("\n ==================")