'''Q24. Use super()

Create:

Person
   ↓
Student

The Person constructor should initialize:

name
age

The Student constructor should initialize:

course

Use super() to call the parent constructor.
'''

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):

    def __init__(self,name,age,course):

        super().__init__(name,age)
        self.course = course

    def display_info(self):

        print(f"Nmae:{self.name}")
        print(f"Age:{self.age}")
        print(f"Course:{self.course}")

s1 = Student("JOHN",23,"DS" )
s1.display_info()
