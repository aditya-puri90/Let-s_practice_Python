"""
Q22. Static Method

Create a class MathUtils with a static method:
    is_even(number)
It should return True if the number is even.
"""


class MathUtils:
    @staticmethod
    def is_even(number):
        return number % 2 == 0


if __name__ == "__main__":
    print("Is 10 even?", MathUtils.is_even(10))
    print("Is 7 even?", MathUtils.is_even(7))
