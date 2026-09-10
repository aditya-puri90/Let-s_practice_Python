"""
Q10. Find Even Numbers Using filter()

Given:
    numbers = [10, 15, 20, 25, 30, 35, 40]
Use filter() to get only even numbers.
"""

numbers = [10, 15, 20, 25, 30, 35, 40]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

if __name__ == "__main__":
    print("Original list:", numbers)
    print("Even numbers:", even_numbers)
