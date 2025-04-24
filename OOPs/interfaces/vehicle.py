"""
    In objected oriented programming interface is a crucial concept
    that defines a contract for classes to follow.

    It allows multiple classes to share a common structure while
    enforcing certain behaviours.

    While python doesn't have inbuilt support for interfaces in java
    It achieves same functionality using abstract base classes(ABCs)
    from abc module.


    An interface defines methods/behaviours that a  class must implement.
    It defines a contract that implementing classes mush adhere to.

    Characteristics:-
    1. Uses abc module in python to create Abstract Base Classes
    2. Defines methods without implementation that must be implemented
    3. Supports multiple inheritance, unlike normal classes
    4. Improves code flexibility and maintainability
"""

"""
    Defining an interface in python
    
    We use ABC class and abstractmethod from abc module in python
"""

from abc import ABC, abstractmethod

# interface name vehicle
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass # just definition no implementation

    def stop(self):
        pass # just definition no implementation



