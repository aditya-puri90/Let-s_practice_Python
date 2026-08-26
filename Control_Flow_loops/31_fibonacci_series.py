'''Q31. Fibonacci Series

Take N and print the first N Fibonacci numbers.'''

N = int(input("Enter N: "))

a, b = 0, 1
for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b
print()
