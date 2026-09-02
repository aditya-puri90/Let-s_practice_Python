"""
Q5. Even or Odd Checker

Create a function check_even_odd(n) that returns:
"Even" or "Odd"
"""

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("10 is:", check_even_odd(10))
print("33 is:", check_even_odd(33))
