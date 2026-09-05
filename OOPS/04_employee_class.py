'''
Q4. Employee class

Create an Employee class with:

name
salary
department

Create an object and display the information.

'''

class Employee:

    def __init__(self, name,salary,dept):

        self.name= name
        self.salary = salary
        self.dept = dept

    def display_info(self):

            print(f"Name:{self.name}, Salary: {self.salary}, Department:{self.dept}")


e1 = Employee("JOHN", 35000,"IT")

e1.display_info()
            
