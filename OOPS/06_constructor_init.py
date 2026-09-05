'''
Q6. Constructor

Create a Student class using __init__() to initialize:

name
age
course

Create an object and print the values.
'''

class Student:

    def __init__(self,name,age,course):

        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"Name:{self.name}, Age:{self.age}, Course:{self.course}")

s1 = Student("JON",20,"BSC")

s1.display_info()