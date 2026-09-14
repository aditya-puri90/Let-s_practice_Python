"""
Q26. Static vs Class vs Instance Method

Create a class Employee containing:
    - an instance method
    - a static method
    - a class method
Demonstrate how each one is called.
"""


class Employee:
    company = "ABC Corp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company}")

    @staticmethod
    def is_valid_salary(salary):
        return salary >= 0

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
        print(f"Company changed to {cls.company}")


if __name__ == "__main__":
    emp1 = Employee("Aditya", 50000)
    emp1.show_info()

    print("Is 30000 valid salary?", Employee.is_valid_salary(30000))
    print("Is -1000 valid salary?", Employee.is_valid_salary(-1000))

    Employee.change_company("XYZ Ltd")
    emp1.show_info()
