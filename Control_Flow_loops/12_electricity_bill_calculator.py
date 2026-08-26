'''Q12. Electricity Bill

Take electricity units and calculate the bill:
0–100 units    -> ₹5/unit
101–200 units  -> ₹7/unit
201–300 units  -> ₹10/unit
Above 300 units -> ₹15/unit'''

units = int(input("Enter the units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
elif units <= 300:
    bill = units * 10
else:
    bill = units * 15

print("Electricity Bill =", bill)
