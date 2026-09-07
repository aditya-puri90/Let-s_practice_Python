"""
Q4. Student Details Using **kwargs

Create a function:
    student_details(**kwargs)
and pass:
    name="Aditya", age=21, course="BSc CS", city="Pune"
Print all key-value pairs.
"""


def student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    student_details(name="Aditya", age=21, course="BSc CS", city="Pune")
