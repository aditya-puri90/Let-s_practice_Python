'''
Q21. Vehicle → Car

Create a parent class Vehicle with:

brand
speed

Create a child class Car with:

model

Display all details.

'''

class Vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

class Car(Vehicle):

    def __init__(self,brand,speed,model):
        super().__init__(brand,speed)

        self.model= model

    def display_info(self):
        print(f"Brand:{self.brand}")
        print(f"Speed:{self.speed}")
        print(f"model:{self.model}")


c1= Car("VW",250,"Virtus")
c1.display_info()            

                