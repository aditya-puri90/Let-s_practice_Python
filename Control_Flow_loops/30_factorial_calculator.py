'''Q30. Factorial

Take a number and calculate its factorial.'''

num = int(input("Enter number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} = {factorial}")
