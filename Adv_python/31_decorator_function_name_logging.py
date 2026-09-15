"""
Q31. Decorator With Function Name Logging

Create a decorator that prints:
    Function name: <function_name>
before executing any function.
"""


def show_function_name(func):
    def wrapper(*args, **kwargs):
        print(f"Function name: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@show_function_name
def greet():
    print("Hello, Welcome!")


@show_function_name
def add(a, b):
    return a + b


if __name__ == "__main__":
    greet()
    print("Result:", add(10, 5))
