"""
Q25. Class Method as Alternative Constructor

Create a class Student with:
    name, age, course
Create a class method:
    from_string(student_str)
that creates an object from:
    "Aditya,21,BSc CS"
"""


class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    @classmethod
    def from_string(cls, student_str):
        name, age, course = [part.strip() for part in student_str.split(",")]
        return cls(name, int(age), course)

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}")


if __name__ == "__main__":
    s1 = Student.from_string("Aditya,21,BSc CS")
    s1.display_info()
