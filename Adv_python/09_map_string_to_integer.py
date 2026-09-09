"""
Q9. Convert Strings to Integers

Given:
    numbers = ["10", "20", "30", "40"]
Use map() to convert them into integers.
"""

numbers = ["10", "20", "30", "40"]
integers = list(map(int, numbers))

if __name__ == "__main__":
    print("String numbers:", numbers)
    print("Integer numbers:", integers)
