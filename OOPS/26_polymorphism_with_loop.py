'''Q28. Polymorphism with a loop

Create:

Dog
Cat
Cow

Each class should have a sound() method.

Store the objects in a list and use a loop to call:

animal.sound()

for every object.'''


class Dog:
    def sound(self):
        print("Dog barks: Woof ")

class Cat:
    def sound(self):
        print("Cat Meows:meow")

class Cow:
    def sound(self):
        print("Cow moose: moo")

animals = [Dog(),Cat(),Cow()]

for animal in animals:
    animal.sound()

        

