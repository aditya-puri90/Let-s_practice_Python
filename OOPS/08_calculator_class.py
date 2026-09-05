'''
Q8. Calculator class

Create a Calculator class with methods:

add()
subtract()
multiply()
divide()

Create an object and perform all four operations.

'''

class Calculator:

    def __init__(self):

        pass
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def division(self,a,b):

       if b!= 0:
           
        return a/b

       else:
          return "Error"


cal = Calculator()

print("Addition:",cal.add(10,5))
print("Subtraction:",cal.subtract(10,5))
print("Multiply:",cal.multiply(10,5))
print("Division:",cal.division(10,5))
    