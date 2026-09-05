'''Q29. Abstract Shape class ⭐

Using Python's abc module, create an abstract class:

Shape

with an abstract method:

area()

Create child classes:

Circle
Rectangle

Implement area() in both classes.'''

from abc import ABC,abstractmethod

class Shapes(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shapes):

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14 *( self.radius **2)

class Rectangle(Shapes):
    def __init__(self,length,width):
        self.length =length
        self.width = width

    def area(self):
        return self.length * self.width


Shapes =[Circle(7),Rectangle(10,5)]

for shape in Shapes:
    print(f"{shape.__class__.__name__} Area:{shape.area()}")