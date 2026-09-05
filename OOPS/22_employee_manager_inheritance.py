'''Q22. Employee → Manager

Create:

Employee
    ↓
Manager

Employee has:

name
salary

Manager has:

team_size

Display all information.'''

class Employee:

    def __init__(self,name,salary):
        self.name= name
        self.salary=salary

class Manager(Employee):

    def __init__(self, name, salary,team_size):

        super().__init__(name,salary)

        self.team_size=team_size

    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Salary:{self.salary}")
        print(f"team Size:{self.team_size}")

m1 = Manager("Tara",700000,3)
m1.display_info()        
        