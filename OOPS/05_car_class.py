'''
Q5. Car class

Create a Car class with:

brand
model
price

Create two car objects and print their details.

'''

class Car:

    def __init__(self,brand,model,price):

        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):

        print(f"Brand: {self.brand}. Model : {self.model} . Price:{self.price}")

c1 = Car("MG","HECTOR",150000)

c2= Car("Tata","Safari",200000)

c1.display_info()
c2.display_info()