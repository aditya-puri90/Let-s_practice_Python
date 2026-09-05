
'''Q26. Method overriding

Create a parent class Animal with:

sound()

Create:

Dog
Cat
Cow

Override sound() in each class with a different sound.'''

class Animal:

    def sound(self):
        print("This Animal makes Sounds.")

class Dog(Animal):
    def sound(self):
        print("Dog barks: woof.")

class Cat(Animal):
    def sound(self):
        print("Cat Meows:moe")

class Cow(Animal):
    def sound(self):
        print("Cow moose: moo")

d1 =Dog()
c1 =Cat()
cw1=Cow()

d1.sound()
c1.sound()
cw1.sound()

