'''
Q2. Student information

Create a Student class with attributes:

name
age
course

Create an object and print all the information.
'''

class Student:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"Student name is {self.name}.this is {self.age} years old  and pursuing {self.course}. ")

# Creating the object for Student class

s1= Student("JOHN DOE",23, "BSC CS")
s1.display_info()
