"""
Q3. Count Arguments

Create a function:
    count_args(*args)
that returns the number of arguments passed.
"""


def count_args(*args):
    return len(args)


if __name__ == "__main__":
    print("Arg count (10, 20, 30, 40):", count_args(10, 20, 30, 40))
    print("Arg count ('a', 'b'):", count_args('a', 'b'))
    print("Arg count ():", count_args())
