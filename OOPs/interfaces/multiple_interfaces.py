"""
    multiple inheritance is supported in python with the help of interfaces
"""

from abc import ABC, abstractmethod

# first interface
class Flying(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def run(self):
        pass # not necessary to have it

# second interface
class Running(ABC):
    @abstractmethod
    def run(self):
        pass

class Car(Flying, Running):
    def fly(self):
        print("car flies...")

    def run(self):
        print("car runs...")

if __name__ == "__main__":
    car = Car()
    car.fly()
    car.run()


