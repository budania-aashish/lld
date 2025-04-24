"""
    💡 Example: Adding logging, authentication, or retries dynamically without touching core logic.
       When to use :
        - You want to add responsibilities dynamically without altering the original class.
        - You want to avoid deep inheritance hierarchies.
        - You have many combinable features (e.g., GUI widgets, coffee toppings, file filters)

"""

from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass

class SimpleCoffee(Coffee):
    def get_cost(self) -> int:
        return 5


class CoffeeDecorator(Coffee):
    _coffee = None
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def get_cost(self) -> int:
        return self._coffee.get_cost()

class MilkDecorator(CoffeeDecorator):
    def get_cost(self)->int:
        return super().get_cost() + 2

class SugarDecorator(CoffeeDecorator):
    def get_cost(self)->int:
        return super().get_cost() + 1


if __name__ == '__main__':
    coffee  = SimpleCoffee()
    print(f"Simple coffee cost : {coffee.get_cost()}")
    coffee = MilkDecorator(coffee)
    print(f"Cost of added milk coffee : {coffee.get_cost()}")
    coffee = SugarDecorator(coffee)
    print(f"Cost of added sugar coffee is : {coffee.get_cost()}")

