"""
Q23. Static Calculator

Create a class Calculator with static methods:
    add(), subtract(), multiply(), division()
Call them without creating an object.
"""


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero."


if __name__ == "__main__":
    print("Add (10, 5):", Calculator.add(10, 5))
    print("Subtract (10, 5):", Calculator.subtract(10, 5))
    print("Multiply (10, 5):", Calculator.multiply(10, 5))
    print("Division (10, 5):", Calculator.division(10, 5))
    print("Division (10, 0):", Calculator.division(10, 0))
