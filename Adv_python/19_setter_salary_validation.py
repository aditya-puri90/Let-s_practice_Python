"""
Q19. Setter Validation

Create a class Employee with private variable:
    __salary
The setter should reject a negative salary.
"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = None
        self.set_salary(salary)

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
            print(f"Salary updated to {salary}")
        else:
            print("Error: Salary cannot be negative!")

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.__salary}")


if __name__ == "__main__":
    e1 = Employee("Aditya", 50000)
    e1.display_info()

    e1.set_salary(-5000)
    e1.set_salary(60000)
    e1.display_info()
