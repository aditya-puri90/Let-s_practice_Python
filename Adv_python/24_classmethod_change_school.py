"""
Q24. Class Method

Create a class Student with a class variable:
    school_name = "ABC College"
Create a class method:
    change_school(new_name)
that changes the school name.
"""


class Student:
    school_name = "ABC College"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name
        print(f"School name changed to {cls.school_name}")

    def display_info(self):
        print(f"Name: {self.name}, School: {Student.school_name}")


if __name__ == "__main__":
    s1 = Student("Aditya")
    s1.display_info()

    Student.change_school("XYZ College")
    s1.display_info()
