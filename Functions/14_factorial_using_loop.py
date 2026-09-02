"""
Q14. Factorial Function (Iterative)

Create factorial(n) calculating factorial using a loop and returning the result.
Example: 5! = 120
"""

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("5! =", factorial(5))
