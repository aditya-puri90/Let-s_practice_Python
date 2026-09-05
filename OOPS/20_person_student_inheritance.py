'''
Q20. Person → Student

Create:

Person
   ↓
Student

Person should contain:

name
age

Student should contain:

course
college

Display all information.

'''

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self,name,age,course,college):

        super().__init__(name,age)
        self.course =course
        self.college = college

    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Course:{self.course}")
        print(f"College:{self.college}")

s1 =Student("Ram",20,"DS","SPPU")
s1.display_info()        
                    
        