"""
    When you have a constructor with tons of parameters (some optional, some required),
    it becomes hard to manage and read.

    Instead of :
    car = Car(wheels=4, color='red', engine='V8', sunroof=True, gps=False, spoiler=False)

    we could use:
    car = CarBuilder().set_wheels(4).set_color('red').set_engine('V8').add_sunroof().build()

    Benefits:
    - Enforces consistency among products.
    - Easy to switch between product families.
    - Follows the Open/Closed Principle.

    Drawbacks:
    - Can be overkill for simple use cases.
    - Adds more classes and complexity.
"""

class Car:
    def __init__(self):
        self.wheels = None
        self.color = None
        self.engine = None
        self.sunroof = None
        self.gps = None

    def __str__(self):
        print(f"car with wheels {self.wheels} of color {self.color}, of engine - {self.engine} "
              f"has sunroof ?- {self.sunroof} has gps? - {self.gps}")

class CarBuilder:
    def __init__(self):
        self.car = Car

    def set_wheels(self, number):
        self.car.wheels = number
        return self

    def set_color(self, color):
        self.car.color = color
        return self.car

    def set_engine(self, engine):
        self.car.engine = engine
        return self.car

    def set_sunroof(self, is_sunroof):
        self.car.sunroof = is_sunroof
        return self.car

    def set_gps(self, is_gps):
        self.car.is_gps = is_gps
        return self.car


# client code
car_builder = CarBuilder()

