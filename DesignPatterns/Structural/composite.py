"""
    The Composite Design Pattern is a structural design pattern used to treat individual
    objects and compositions of objects uniformly. It's especially useful when dealing with
    tree-like structures such as file systems, GUI components, or organizational hierarchies.

    Key Concepts
    - Component: An abstract class/interface for all objects in the composition.
    - Leaf: Represents leaf objects in the composition (no children).
    - Composite: Represents a node that can have children (other Component objects).
"""


from abc import ABC, abstractmethod

# Component
class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass

# Leaf
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print(' ' * indent + self.name)

# Composite
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def display(self, indent=0):
        print(' ' * indent + f"[{self.name}]")
        for child in self.children:
            child.display(indent + 2)

# Example usage
if __name__ == "__main__":
    root = Directory("root")
    root.add(File("file1.txt"))
    root.add(File("file2.txt"))

    sub_dir = Directory("subdir")
    sub_dir.add(File("file3.txt"))

    root.add(sub_dir)

    root.display()
