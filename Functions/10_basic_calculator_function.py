"""
Q10. Calculator Function

Create calculator(a, b, operator) supporting '+', '-', '*', '/'.
"""

def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b if b != 0 else "Error: Division by zero"
    else:
        return "Invalid operator"

print("10 + 24 =", calculator(10, 24, "+"))
print("20 - 7  =", calculator(20, 7, "-"))
print("6 * 8   =", calculator(6, 8, "*"))
print("45 / 9  =", calculator(45, 9, "/"))
