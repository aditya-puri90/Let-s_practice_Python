"""
Q17. Basic Getter

Create a class Student with a private variable:
    __name
Create a getter method:
    get_name()
to access the name.
"""


class Student:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


if __name__ == "__main__":
    s1 = Student("Aditya")
    print("Student Name:", s1.get_name())
