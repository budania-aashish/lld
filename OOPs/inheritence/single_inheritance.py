# single level
class Animal:
    def __init__(self, name):
        self.name = name

    def eats(self):
        print("Animal {0} eats".format(self.name))

class Dog(Animal):
    def bark(self):
        print("Dog {0} barks...".format(self.name))

if __name__ == "__main__":
    dog = Dog("Tommy")
    dog.bark()
    dog.eats()