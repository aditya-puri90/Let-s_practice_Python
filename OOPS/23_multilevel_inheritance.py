'''Q23. Multilevel inheritance

Create:

Animal
   ↓
Mammal
   ↓
Dog

Give each class at least one method.

Create a Dog object and call methods from all three classes.'''

class Animal:

    def eat(self):
        print("This Animal is Eating")

class Mammal(Animal):

    def drink(self):

        print("This Mammel are Drinkong")

class Dog(Mammal):

    def bark(self):
        print("This Dog is Barking.")


    

d1 = Dog()   

d1.eat()
d1.drink()
d1.bark()