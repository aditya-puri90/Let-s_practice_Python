"""
Q5. Combine *args and **kwargs

Create:
    def student(*args, **kwargs):
Pass subjects through *args and student information through **kwargs.
Print both.
"""


def student(*args, **kwargs):
    print("Subjects:")
    for subject in args:
        print(f"  - {subject}")

    print("\nStudent Information:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    student("Math", "Physics", "Chemistry", name="Aditya", age=21, course="BSc CS", city="Pune")
