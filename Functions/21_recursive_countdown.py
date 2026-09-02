"""
Q21. Recursive Countdown

Create a recursive function that counts down from N to 0.
"""

def countdown(n):
    if n < 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

countdown(5)
