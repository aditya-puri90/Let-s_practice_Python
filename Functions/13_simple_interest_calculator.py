"""
Q13. Simple Interest Calculator

Create simple_interest(principal, rate, time) returning:
SI = (P * R * T) / 100
"""

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

si = simple_interest(100000, 4, 9)
print("Simple Interest:", si)
