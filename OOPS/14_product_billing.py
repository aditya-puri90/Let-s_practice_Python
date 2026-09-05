'''
Q14. Product class

Create a Product class with:

product name
price
quantity

Create a method total_price() that returns:

price × quantity

'''

class Product:
    def __init__(self,product_name,price,quantity):
        self.product_name = product_name
        self.price=price
        self.quantity=quantity

    def total_price(self):
            return self.price * self.quantity

    def display_info(self):
        print(f"Product name:{self.product_name}")
        print(f"Price:{self.price}")
        print(f"quantity:{self.quantity}")
        print(f"Total Price:{self.total_price()}")

p1= Product("Parle-G",5,100)
p1.display_info()  