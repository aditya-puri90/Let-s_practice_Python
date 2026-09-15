"""
Q29. Execution Time Decorator

Create a decorator that measures approximately how long a function takes to execute.
Use:
    import time
Test it with a function containing a loop.
"""

import time


def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper


@execution_time
def loop_function(n):
    total = 0
    for i in range(n):
        total += i
    return total


if __name__ == "__main__":
    result = loop_function(100000)
    print("Result:", result)
