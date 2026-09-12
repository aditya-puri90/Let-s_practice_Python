"""
Q13. Calculate Total Using reduce()

Given:
    numbers = [10, 20, 30, 40]
Use reduce() to calculate the total sum.
"""

from functools import reduce

numbers = [10, 20, 30, 40]
total_sum = reduce(lambda x, y: x + y, numbers)

if __name__ == "__main__":
    print("Numbers:", numbers)
    print("Total sum:", total_sum)
