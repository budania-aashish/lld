"""
    Unlike java python doesn't have default methods for interfaces,
    But we could add our default methods in base classes(that uses ABC)
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eats(self):
        pass

    def sleeps(self): # default method
        print("Animal sleeps...")

class Dog(Animal):
    def eats(self):
        print("Can eat veg or non-veg...")

if __name__ == "__main__":
    dog = Dog()
    dog.eats()
    dog.sleeps()