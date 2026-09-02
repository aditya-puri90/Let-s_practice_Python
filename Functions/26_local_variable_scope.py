"""
Q26. Local Variable Scope

Demonstrates local variable scope inside a function.
Local variables exist only during the function's execution.
"""

def test():
    x = 10
    print("Inside function x =", x)

test()
# print(x)  # NameError: name 'x' is not defined outside test()
