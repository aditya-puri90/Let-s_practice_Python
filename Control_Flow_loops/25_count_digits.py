'''Q25. Count Digits

Take a number and count how many digits it contains.'''

num = int(input("Enter number: "))

count = 0
temp = abs(num)

if temp == 0:
    count = 1
else:
    while temp > 0:
        temp //= 10
        count += 1

print("Number of digits =", count)
