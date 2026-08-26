'''Q22. Sum Until Zero

Keep taking numbers from the user.
Stop when the user enters 0.
Then print the total sum.'''

total = 0

while True:
    n = int(input("Enter number: "))
    if n == 0:
        break
    total += n

print("Total =", total)
