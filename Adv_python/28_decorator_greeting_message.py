"""
Q28. Greeting Decorator

Create:
    @greet_decorator
    def hello():
        print("Hello")

The decorator should print:
    "Welcome to Python!"
before executing hello().
"""


def greet_decorator(func):
    def wrapper():
        print("Welcome to Python!")
        return func()
    return wrapper


@greet_decorator
def hello():
    print("Hello")


if __name__ == "__main__":
    hello()
