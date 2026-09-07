"""
Q2. Find Maximum Using *args

Create a function:
    maximum(*args)
that returns the largest number without using max().
"""


def maximum(*args):
    if not args:
        return None

    largest = args[0]
    for num in args[1:]:
        if num > largest:
            largest = num
    return largest


if __name__ == "__main__":
    print("Maximum (10, 20, 30, 40):", maximum(10, 20, 30, 40))
    print("Maximum (-5, -2, -10):", maximum(-5, -2, -10))
