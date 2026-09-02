"""
Q28. Local vs Global Variable Shadowing

Demonstrates variable shadowing where a local variable with the same name
shadows the global variable within the function scope.
"""

x = 10

def test():
    x = 20
    print("Inside (local):  ", x)

test()
print("Outside (global):", x)
