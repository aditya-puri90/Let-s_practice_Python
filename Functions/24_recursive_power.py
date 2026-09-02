"""
Q24. Recursive Power Function

Create power(base, exponent) using recursion:
base^exponent = base * base^(exponent - 1)
"""

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print("2^5 =", power(2, 5))
