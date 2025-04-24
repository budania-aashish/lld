"""
    Software entities (classes, modules, functions, etc.) should be open for extension,
    but closed for modification.

    This means the design of a software entity should be such that you can introduce
    new functionality or behavior without modifying the existing code since changing
    the existing code might introduce bugs.

"""

class ShapeCalculator:
    def calculate_area(self, shape):
        print(f"class :  {self.__class__}")
        if shape.type == "rectangle":
            return shape.width * shape.height

        if shape.type == "circle":
            return 3.14 * shape.radius * shape.radius

    def calculate_perimeter(self, shape):
        print(f"class :  {self.__class__}")
        if shape.type == "rectangle":
            return 2*(shape.width * shape.height)

        if shape.type == "circle":
            return 2*3.14*shape.radius

"""
    Now if we want to add triangle calculation we have to modify ShapeCalculator but we don't want to do that
    
    So we can make an interface named Shape, and have different implementation for each of these
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * pow(self.radius, 2)

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        half_perimeter = self.calculate_perimeter()/2
        return sqrt(half_perimeter*(half_perimeter-self.side1)*(half_perimeter-self.side2)*(half_perimeter-self.side3))

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
"""
    By introducing an abstraction (Shape class) and separating the concrete implementations 
    (Rectangle and Circle classes), we can add new shapes without modifying the existing code.
    
    The ShapeCalculator class can now work with any shape that implements the Shape interface, 
    allowing for easy extensibility.
    
"""
