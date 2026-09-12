"""
Q15. Find Largest Using reduce()

Use reduce() to find the largest number in:
    numbers = [45, 12, 78, 34, 89, 23]
"""

from functools import reduce

numbers = [45, 12, 78, 34, 89, 23]
largest = reduce(lambda x, y: x if x > y else y, numbers)

if __name__ == "__main__":
    print("Numbers:", numbers)
    print("Largest number:", largest)
