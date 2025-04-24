"""
    Why to prefer composition instead inheritance?

    - Encapsulation & Flexibility
        - composition allows use to change the behaviours of the object dynamically by changing the components at runtime
        - Inheritance makes it difficult to change an existing class hierarchy without breaking existing code

    - Better Code Reusability
        - composition provide reusability as the same component can be used at multiple place
        - for example - engine, transmission, wheel could be used for car, bike, truck etc

    - Avoids Inheritance Pitfalls
        - Inheritance can lead to deep class hierarchy, making maintenance difficult
        - It enforces parent-child strict relationship, that can be too rigid for some designs

    - Supports Interface-Based Design
        - Composition can be combined with interface(abstract classes) to achieve powerful decoupling
"""

from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass # abstract method

    @abstractmethod
    def get_engine_name(self):
        pass # abstract method

class PetrolEngine(Engine):
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"Engine {self.name} starts!")

    def get_engine_name(self):
        return self.name

class DieselEngine(Engine):
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"Engine {self.name} starts!")

    def get_engine_name(self):
        return self.name

class Car:
    def __init__(self, car_engine):
        self.engine = car_engine

    def drive(self):
        self.engine.start()
        print(f"Car drives of {self.engine.get_engine_name()}")

if __name__ == '__main__':
    engine = PetrolEngine("petrol engine")
    car = Car(engine)
    car.drive()

    engine = DieselEngine("diesel engine")
    car = Car(engine)
    car.drive()

