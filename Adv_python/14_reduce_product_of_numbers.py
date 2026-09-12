"""
Q14. Find Product Using reduce()

Given:
    numbers = [1, 2, 3, 4, 5]
Use reduce() to calculate: 1 * 2 * 3 * 4 * 5
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)

if __name__ == "__main__":
    print("Numbers:", numbers)
    print("Product:", product)
