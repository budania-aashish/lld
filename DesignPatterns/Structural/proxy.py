"""
    The Proxy Design Pattern is a structural design pattern that provides a placeholder or
    surrogate for another object to control access to it. It’s commonly used for lazy
    initialization, access control, logging, caching, etc.


    Subject (Interface):
    - Common interface for Real and Proxy.
    RealSubject:
    - The actual object that performs operations.
    Proxy:
    - Controls access to the RealSubject, adds logic (e.g. logging, access checks).

"""

from abc import ABC, abstractmethod

# Subject
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# RealSubject
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_image_from_disk()

    def load_image_from_disk(self):
        print(f"Loading image from disk: {self.filename}")

    def display(self):
        print(f"Displaying image: {self.filename}")

# Proxy
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

# Example usage
if __name__ == "__main__":
    image1 = ProxyImage("photo1.png")
    image2 = ProxyImage("photo2.png")

    print("Accessing image1:")
    image1.display()  # Loads and displays

    print("\nAccessing image1 again:")
    image1.display()  # Only displays

    print("\nAccessing image2:")
    image2.display()
