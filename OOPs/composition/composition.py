"""
    Composition: One of core principle of OOPs. It is practice of building objects
    using other objects, promoting code reuse, flexibility and maintainability.

    Unlike inheritance that works based on Is-A relationship, it works on Has-A relationship.

    Here an object consists of an instance or multiple instances of another class.

    The contained class is often called as a component, and the containing class is called
    a composite class.

    This helps in building complex systems by combining the simpler objects.

"""

"""
    When to use composition?
    - When building complex objects that consist of multiple objects
    - When want to achieve code reusability without complex hierarchical inheritance
    - When different behaviours needs to be used dynamically (different type of engines in a car)
    - When following the favor composition over inheritance principle
"""

"""
Example : Car and its components 
"""

class Car:
    def __init__(self, car_engine, car_wheels, car_transmission):
        self.engine = car_engine
        self.wheel = car_wheels
        self.transmission = car_transmission

    def drive(self):
        self.engine.start()
        self.wheel.rotate()
        self.transmission.change()
        print(f"Car started...!")

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

    def start(self):
        print(f"Started engine with Horse Power {self.horse_power}")

class Wheel:
    def __init__(self, wheel_type):
        self.wheel_type = wheel_type

    def rotate(self):
        print(f"Rotation started for {self.wheel_type}")

class Transmission:
    def __init__(self, transmission_type):
        self.transmission_type = transmission_type

    def change(self):
        print(f"Transmission {self.transmission_type} changes")


if __name__ == '__main__':
    engine = Engine(150)
    wheel = Wheel("Alloy")
    transmission = Transmission("Manual")

    car = Car(engine, wheel, transmission)
    car.drive()