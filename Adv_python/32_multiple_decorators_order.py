"""
Q32. Multiple Decorators

Create two decorators:
    @decorator1
    @decorator2
Apply both to the same function and observe the execution order.
"""


def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1: Before function")
        result = func(*args, **kwargs)
        print("Decorator 1: After function")
        return result
    return wrapper


def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2: Before function")
        result = func(*args, **kwargs)
        print("Decorator 2: After function")
        return result
    return wrapper


@decorator1
@decorator2
def my_function():
    print("Original function is running!")


if __name__ == "__main__":
    my_function()
