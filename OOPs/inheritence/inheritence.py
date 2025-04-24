"""
    Inheritance: inheritance is one of the core principle of OOP
    It allows a class(subclass/child class) to acquire and use the
    properties/fields & behaviours/methods/functions of the another
    class (parent or super class). This promotes code reusability,
    maintainability, scalability.

    Inheritance: Property in which subclass/child class can use the
    properties and behaviours of the parent class or super class.

    A subclass can
    - use attributes and behaviours of the superclass
    - override the behaviour of a parent class for specific implementation
    - can add its own attributes and behaviours

    Benefits -
    - Code Reusability : Avoid code duplication by using attributes
                        and behaviours of the parent class
    - Improves Maintainability : Reduces redundancy of the code making
                       it easier to manage
    - Enhances Extensibility : Makes code easier to extend in case of
                        new functionality
"""

# parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("{0} is eating...".format(self.name))

# child class
class Dog(Animal):
    def bark(self):
        print("Dog barks...")

if __name__ == "__main__":
    dog = Dog("Tom") # constructor also used from parent class
    dog.bark() # additional behaviour in the child class
    dog.eat() # behaviour used of parent class

