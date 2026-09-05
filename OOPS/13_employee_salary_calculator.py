'''
Create an Employee class with:

name
basic salary

Create methods to calculate:

HRA = 20% of salary
DA = 10% of salary
Total Salary
'''
class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def hra(self):
        return 0.20 * self.basic_salary   # 20% of salary

    def da(self):
        return 0.10 * self.basic_salary   # 10% of salary

    def total_salary(self):
        return self.basic_salary + self.hra() + self.da()

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Basic Salary: {self.basic_salary}")
        print(f"HRA: {self.hra()}")
        print(f"DA: {self.da()}")
        print(f"Total Salary: {self.total_salary()}")



emp1 = Employee("John Doe", 50000)
emp1.display_info()
