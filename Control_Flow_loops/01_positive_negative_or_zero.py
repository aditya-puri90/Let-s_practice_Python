'''Q1. Positive, Negative or Zero

Take a number from the user and check whether it is:
- Positive
- Negative
- Zero'''

num = int(input("Enter the number: "))

if num > 0:
    print("The given number is positive.")
elif num == 0:
    print("The given number is zero.")
else:
    print("The given number is Negative.")
