'''
Q7. self keyword

Create a class Person with name and age.

Use self correctly inside the constructor.
'''

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name :{self.name}, Age : {self.age}")

p1 = Person("JON",23)

p1.display_info()