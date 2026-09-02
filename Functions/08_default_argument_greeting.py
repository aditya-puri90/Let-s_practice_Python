"""
Q8. Default Arguments

Create greet(name, message="Good Morning")
- If message is omitted: "Hello <name>, Good Morning"
- If message is provided: "Hello <name>, <message>"
"""

def greet(name, message="Good Morning"):
    print(f"Hello {name}, {message}")

greet("Aditya")
greet("Aditya", "Good Evening")
