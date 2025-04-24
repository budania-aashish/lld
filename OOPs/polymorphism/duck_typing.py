"""
    Duck Typing : Using polymorphism like Duck Typing
    If it looks like duck, quacks like a duck, it's a duck
    That means no need of external interface's presence or implementation

    When to use
    - Promotes loose coupling, making code more flexible
    - Allows multiple implementations of the same behaviour without inheritance 

"""

class Dog:
    def __init__(self, name):
        self.name = name

    def makes_sound(self):
        print(f"{self.name} barks")

class Cat:
    def __init__(self, name):
        self.name = name

    def makes_sound(self):
        print(f"{self.name} meows")

# polymorphic function
def animal_sound(animal_object):
    animal_object.makes_sound()

if __name__ == '__main__':
    animals = [Dog("Tommy"), Cat("Sweetie")]
    for animal in animals:
        animal_sound(animal)
