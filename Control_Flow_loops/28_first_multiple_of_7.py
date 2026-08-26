'''Q28. First Multiple of 7

Print numbers from 1 to 100 and stop when you find the first number divisible by 7.'''

for i in range(1, 101):
    if i % 7 == 0:
        print("First number divisible by 7 =", i)
        break
