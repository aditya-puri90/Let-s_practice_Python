'''
Q15. Library Book

Create a Book class with:

title
author
price

Create a method display() to display book details.

Create at least 3 book objects.
'''

class Book:
    def __init__(self,title,auther,price):
        self.title = title
        self.auther = auther
        self.price = price

    def display(self):
            print(f"Title:{self.title}")
            print(f"Auther {self.auther}")
            print(f"Price:{self.price}")
            print(f" "*30)

b1=Book("C","Danis",200)
b2=Book("Python","Gudio",280)
b3=Book("Mahabharat","Valmik",1000)

b1.display()
b2.display()
b3.display()