"""
Q7. Square Using map()

Given:
    numbers = [1, 2, 3, 4, 5]
Use map() to generate squares: [1, 4, 9, 16, 25]
"""

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))

if __name__ == "__main__":
    print("Original numbers:", numbers)
    print("Squared numbers:", squares)
