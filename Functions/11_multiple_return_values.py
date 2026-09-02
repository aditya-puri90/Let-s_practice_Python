"""
Q11. Multiple Return Values

Create calculate(a, b) that returns addition, subtraction, multiplication, and division.
Unpack the returned values into four variables.
"""

def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else None
    return addition, subtraction, multiplication, division

add, sub, mul, div = calculate(20, 5)

print("Addition:      ", add)
print("Subtraction:   ", sub)
print("Multiplication:", mul)
print("Division:      ", div)
