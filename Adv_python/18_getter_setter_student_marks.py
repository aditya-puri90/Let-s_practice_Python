"""
Q18. Getter and Setter

Create a class Student with private variable:
    __marks
Create:
    get_marks()
    set_marks()
Only allow marks between 0 and 100.
"""


class Student:
    def __init__(self, name, marks=0):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print(f"Marks updated to {marks}")
        else:
            print("Invalid marks! Must be between 0 and 100")

    def display_info(self):
        print(f"Name: {self.name}, Marks: {self.__marks}")


if __name__ == "__main__":
    s1 = Student("Aditya", 80)
    s1.display_info()
    print("Current Marks:", s1.get_marks())

    s1.set_marks(95)
    s1.set_marks(120)
    s1.display_info()
