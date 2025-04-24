"""
    The Bridge design pattern is a structural pattern that decouples an abstraction from
    its implementation so that the two can vary independently. It's useful when you want
    to avoid a permanent binding between an abstraction and its implementation, especially
    when both can be extended separately.

    When to use :
    - When you want to avoid a permanent binding between an abstraction and its implementation.
    - When both the abstraction and implementation should be independently extensible.
    - When changes in the implementation of an abstraction should not impact clients.
"""


from abc import ABC, abstractmethod

# Implementer Interface
class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius):
        pass

# Concrete Implementers
class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle of radius {radius} using vector rendering.")

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle of radius {radius} using raster rendering.")

# Abstraction
class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass

# Refined Abstraction
class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: float):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

# Client Code
if __name__ == "__main__":
    vector = VectorRenderer()
    raster = RasterRenderer()

    circle1 = Circle(vector, 5)
    circle2 = Circle(raster, 10)

    circle1.draw()  # Output: Drawing a circle of radius 5 using vector rendering.
    circle2.draw()  # Output: Drawing a circle of radius 10 using raster rendering.
