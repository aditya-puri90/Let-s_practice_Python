"""
Q27. Global Variable Read

Demonstrates reading a global variable inside and outside a function.
"""

x = 20

def test():
    print("Inside function:", x)

test()
print("Outside function:", x)
