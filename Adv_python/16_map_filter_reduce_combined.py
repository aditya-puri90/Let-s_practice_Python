"""
Q16. Combined map() + filter() + reduce()

Given:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
Perform:
    1. Filter even numbers.
    2. Square the even numbers using map().
    3. Find their sum using reduce().
Expected result:
    120
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even = filter(lambda x: x % 2 == 0, numbers)
squares = map(lambda x: x**2, even)
total = reduce(lambda x, y: x + y, squares)

if __name__ == "__main__":
    print("Original numbers:", numbers)
    print("Sum of squared even numbers:", total)
