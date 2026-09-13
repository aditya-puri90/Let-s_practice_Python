"""
Q20. Using @property

Create a class Person with private:
    __age
Use:
    @property
    @age.setter
to get and set the age. Don't allow age below 0.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = None
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value
            print(f"Age updated to {value}")
        else:
            print("Error: Age cannot be negative!")

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.__age}")


if __name__ == "__main__":
    p1 = Person("Aditya", 25)
    p1.display_info()

    p1.age = -5
    p1.age = 30
    p1.display_info()
