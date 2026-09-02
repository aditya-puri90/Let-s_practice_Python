"""
Q9. Maximum of Three Numbers

Create a function maximum(a, b, c) that returns the largest number without using max().
"""

def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("Maximum:", maximum(10, 23, 90))
