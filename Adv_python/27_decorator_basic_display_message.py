"""
Q27. Basic Decorator

Create a decorator called:
    @display_message
that prints:
    "Function is being executed"
before calling the original function.
"""


def display_message(func):
    def wrapper():
        print("Function is being executed")
        return func()
    return wrapper


@display_message
def greet():
    print("Hello, welcome!")


if __name__ == "__main__":
    greet()
