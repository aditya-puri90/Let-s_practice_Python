'''
Q3. Multiple objects

Create a Student class and create 3 different student objects with different names and ages.

Print their details
'''

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):   

        print(f"Student name is{self.name} and their age is {self.age}")

s1 = Student("JOHN",23)
s2 = Student("BELLA",24)
s3 = Student("RAM",20)

s1.display_info()
s2.display_info()
s3.display_info()