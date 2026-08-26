'''Q18. Sum of 1 to N

Take N from the user and calculate:
1 + 2 + 3 + ... + N'''

N = int(input("Enter N: "))
total = 0

for i in range(1, N + 1):
    total += i

print("Sum =", total)
