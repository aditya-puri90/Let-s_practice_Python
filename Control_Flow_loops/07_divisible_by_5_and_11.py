'''Q7. Divisible by Both 5 and 11

Take a number and check whether it is divisible by both 5 and 11.'''

a = int(input("Enter the number: "))

if a % 5 == 0 and a % 11 == 0:
    print("The given number is divisible by both 5 and 11.")
else:
    print("Not divisible by both 5 and 11.")
