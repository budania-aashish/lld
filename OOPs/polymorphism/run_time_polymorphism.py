"""
    Method Overriding:
    This happens when a class has specific implementation of a behaviour or a method

    When to use -
    - enables dynamic method resolution
    - supports polymorphic behaviour, where one interface is used for multiple implementation
    - makes code extensible by allowing future modifications 
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def makes_sound(self):
        print(f"Animal {self.name} makes found")

class Dog(Animal):
    def makes_sound(self):
        print(f"Dog {self.name} barks")

class Cat(Animal):
    def makes_sound(self):
        print(f"Cat {self.name} meows")

if __name__ == '__main__':
    animals = [Dog("Tommy"), Cat("Sweetie")]
    for animal in animals:
        animal.makes_sound()
