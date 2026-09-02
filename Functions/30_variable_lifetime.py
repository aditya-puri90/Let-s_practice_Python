"""
Q30. Variable Lifetime & Scope

Demonstrates the lifetime of local variables created on the stack frame.
"""

def test():
    x = 100
    print("Local variable x inside test():", x)

test()
# x is deallocated once test() terminates; accessing x here raises NameError.
