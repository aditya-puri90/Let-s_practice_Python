'''
Q18. Encapsulation with getter/setter

Create a Student class with a private attribute:

__marks

Create:

get_marks()
set_marks()

Don't allow marks greater than 100 or less than 0.
'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # private attribute

    
    def get_marks(self):
        return self.__marks

    
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print(f"Marks updated to {marks}")
        else:
            print("Invalid marks! Must be between 0 and 100.")

    def display_info(self):
        print(f"Name: {self.name}, Marks: {self.__marks}")



s1 = Student("Alice", 85)

s1.display_info()
print("Current Marks:", s1.get_marks())

s1.set_marks(95)     # valid update
s1.set_marks(120)    #  invalid update
s1.display_info()



