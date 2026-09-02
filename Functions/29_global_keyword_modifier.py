"""
Q29. Global Keyword Modifier

Demonstrates using the 'global' keyword to modify a global variable inside a function.
"""

x = 10

def change():
    global x
    x = 50

print("Before function call:", x)
change()
print("After function call: ", x)
