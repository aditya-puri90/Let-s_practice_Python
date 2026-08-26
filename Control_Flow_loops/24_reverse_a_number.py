'''Q24. Reverse a Number

Take a number and reverse it using a while loop.'''

num = int(input("Enter number: "))

reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Output =", reverse)
