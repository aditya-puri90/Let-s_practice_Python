"""
Q6. Flexible Calculator

Create:
    calculator(operation, *args)
Support:
    - addition
    - multiplication
    - subtraction
"""


def calculator(operation, *args):
    if not args:
        return None

    if operation == "add":
        result = 0
        for num in args:
            result += num
        return result
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
        return result
    elif operation == "subtract":
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    else:
        return "Invalid operation!"


if __name__ == "__main__":
    print("Addition (10, 20, 30):", calculator("add", 10, 20, 30))
    print("Multiplication (2, 3, 4):", calculator("multiply", 2, 3, 4))
    print("Subtraction (100, 20, 30):", calculator("subtract", 100, 20, 30))
