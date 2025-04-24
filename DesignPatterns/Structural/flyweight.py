"""
    The Flyweight design pattern is a structural pattern that is used to minimize memory usage
    by sharing as much data as possible with similar objects. It is particularly useful when
    dealing with a large number of objects that share common properties.

    Intrinsic state: Shared between objects (stored in the Flyweight).
    Extrinsic state: Passed in when needed (not stored in the Flyweight).
    Flyweight objects are usually managed by a Factory.

"""

# Flyweight class
class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x, y):
        print(f"Drawing tree '{self.name}' of color '{self.color}' with texture '{self.texture}' at ({x},{y})")

# Flyweight Factory
class TreeFactory:
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        key = (name, color, texture)
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color, texture)
        return cls._tree_types[key]

# Context class using the Flyweight
class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        self.tree_type.draw(self.x, self.y)

if __name__ == '__main__':
    # Usage
    forest = []
    tree_type = TreeFactory.get_tree_type("Oak", "Green", "Rough")
    for i in range(5):
        forest.append(Tree(i, i * 2, tree_type))

    for tree in forest:
        tree.draw()
