"""
Q23. Recursive Sum of 1 to N

Create a recursive function that calculates:
1 + 2 + 3 + ... + N
"""

def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)

print("Sum of 1 to 10:", recursive_sum(10))
