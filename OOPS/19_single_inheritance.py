'''
Q19. Basic inheritance

Create a parent class:

Animal

with a method:

eat()

Create a child class:

Dog

with a method:

bark()

Create a Dog object and call both methods.

'''

class Animal:

    def eat(self):
        print("This animal is eating:")

class Dog(Animal):
    def bark(self):
                print("The dog is barking")

d1 =Dog()

d1.eat()
d1.bark()
