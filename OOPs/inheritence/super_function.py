"""
    super() in python
    - is used to call parent class constructor
    - is used to call parent class methods
"""

class Animal:
    def __init__(self, name):
        print("animal constructor")
        self.name = name

    def eats(self):
        print(f"{self.name} eats")

class Dog(Animal):
    def __init__(self, name):
        # print("dog constructor with name {0}".format(self.name)) -> gives error
        super().__init__(name)
        print("dog constructor with name {0}".format(self.name)) # will print the message


    def barks(self):
        super().eats()
        print(f"{self.name} barks")

if __name__ == '__main__':
    dog = Dog("Tommy")
    dog.barks()




