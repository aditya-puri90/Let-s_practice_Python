'''
Q10. Circle class

Create a Circle class with a radius attribute.

Create methods:

area()
circumference()

Use:

π = 3.14

'''

class Circle:

    def __init__(self,radius):
        self.radius = radius

    def area(self):

        return 3.14 *(self.radius**2)

    def circumference(self):

        return 2*3.14*self.radius

circ1 = Circle(12)

print("Area Of Circle :",circ1.area())

print("circumference of circle :", circ1.circumference())