"""
Q11. Filter Numbers Greater Than 50

Given:
    numbers = [10, 55, 23, 78, 90, 45, 67]
Use filter() to get numbers greater than 50.
"""

numbers = [10, 55, 23, 78, 90, 45, 67]
greater_than_50 = list(filter(lambda x: x > 50, numbers))

if __name__ == "__main__":
    print("Original numbers:", numbers)
    print("Numbers > 50:", greater_than_50)
