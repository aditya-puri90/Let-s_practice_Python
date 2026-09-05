'''
Q12. Student Result

Create a Student class with:

name
marks in 3 subjects

Create methods:

total()
percentage()
grade()

Display the student's complete result.

'''

class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total(self):
        return self.m1 + self.m2 + self.m3

    def percentage(self):
        return (self.total() / 300) * 100   

    def grade(self):
        pct = self.percentage()
        if pct >= 75:
            return "A"
        elif pct >= 60:
            return "B"
        elif pct >= 40:
            return "C"
        else:
            return "Fail"

    def display_result(self):
        print(f"Student: {self.name}")
        print(f"Marks: {self.m1}, {self.m2}, {self.m3}")
        print(f"Total: {self.total()}")
        print(f"Percentage: {self.percentage():.2f}%")
        print(f"Grade: {self.grade()}")



s1 = Student("Alice", 85, 78, 92)
s1.display_result()
