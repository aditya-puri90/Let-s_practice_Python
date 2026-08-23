'''Take an amount in rupees and convert it into:

Rupees
Paise'''

amount = float(int(input("Enter the amount :")))
rupees = int(amount)
paise = int((amount - rupees) * 100)

print("Rupees =",rupees,"Paise =", paise)