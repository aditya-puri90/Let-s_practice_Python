'''Q17. Multiplication Table

Take a number and print its multiplication table from 1 to 10.'''

num = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
