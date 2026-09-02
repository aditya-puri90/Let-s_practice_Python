"""
Q25. Recursive Fibonacci

Create a recursive function fibonacci(n) that returns the nth Fibonacci number.
"""

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("First 10 Fibonacci numbers:")
for i in range(10):
    print(fibonacci(i), end=" ")
print()
