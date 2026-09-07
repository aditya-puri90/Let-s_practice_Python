"""
Q1. *args Basics

Create a function sum_numbers(*args) that accepts any number of numbers and returns their sum.

Example:
    sum_numbers(10, 20, 30, 40) -> 100
"""


def sum_numbers(*args):
    return sum(args)


if __name__ == "__main__":
    result = sum_numbers(10, 20, 30, 40)
    print("Sum of numbers:", result)
