"""
Q30. Login Decorator

Create a decorator:
    @check_login
that checks whether a user is logged in before allowing a function to execute.
If the user is not logged in, print "Please login first".
"""

is_logged_in = False


def check_login(func):
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Please login first")
            return None
    return wrapper


@check_login
def view_dashboard():
    print("Welcome to your dashboard!")


if __name__ == "__main__":
    print("--- Attempt without login ---")
    view_dashboard()

    print("\n--- Attempt after login ---")
    is_logged_in = True
    view_dashboard()
