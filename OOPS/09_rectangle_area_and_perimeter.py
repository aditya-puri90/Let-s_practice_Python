'''
Q9. Rectangle class

Create a Rectangle class with:

length
width

Create methods:

area()
perimeter()

Return the calculated values.
'''
class Rectangle:

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.length + self.width)

rect = Rectangle(10,5)

print("Area of Rectangle :",rect.area())
print("Perimeter of Rectangle:",rect.perimeter())
     