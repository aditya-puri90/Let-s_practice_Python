'''Seconds Converter
Take total seconds as input and convert them into:

Minutes
Remaining seconds'''

total_seconds = float(input("Enter the total seconds:"))

minutes = total_seconds / 60
remaning_sec = total_seconds % 60

print("Minutes =",minutes,"remaning seconds =", remaning_sec)