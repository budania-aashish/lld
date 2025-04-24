"""
    The Prototype Pattern is used to create new objects by copying (cloning)
    existing ones instead of instantiating new ones from scratch.

    Avoids expensive "new" object creation.
    - Can simplify object construction logic.
    - Useful for games, graphics editors, or deep configuration templates.

    Cons:
    - Requires implementation of a clone method in every class.
    - Deep cloning can be tricky with circular references.
"""

import copy
from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass



class Circle(Prototype):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def clone(self):
        copy.deepcopy(self)

    def __str__(self):
        return f"Circle of radius: {self.radius} and color : {self.color}"


if __name__ == '__main__':
    circle = Circle(4, "blue")
    print(circle)
    circle_cloned = Circle(5, "green")
    print(circle_cloned)