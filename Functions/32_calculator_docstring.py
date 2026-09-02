"""
Q32. Docstring for Calculator

Create a calculator function with a comprehensive docstring explaining its purpose, parameters, and return types.
"""

def calculator(a, b, operator):
    """
    Perform basic arithmetic operations on two numbers.

    Parameters:
    a (float/int): The first operand.
    b (float/int): The second operand.
    operator (str): Operation to perform ('+', '-', '*', '/').

    Returns:
    float/int/str: Result of the calculation or error message.
    """
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b if b != 0 else "Error: Division by zero"
    else:
        return "Error: Invalid operator"

print("Result:", calculator(10, 5, "+"))
print("\nDocstring:")
print(calculator.__doc__)
