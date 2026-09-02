"""
Q22. Recursive Factorial

Create factorial(n) using recursion:
n! = n * (n - 1)!
Base case: 0! = 1, 1! = 1
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("3! =", factorial(3))
print("5! =", factorial(5))
