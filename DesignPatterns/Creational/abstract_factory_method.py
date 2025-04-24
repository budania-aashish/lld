"""
    Provides an interface for creating families of related or dependent objects
    without specifying their concrete classes.

    Think of it like a factory of factories. It helps you create objects that
    belong to a particular family, ensuring they are compatible with each other.

    Let's try to make GUI consisting of a button and a checkbox for windows laptop and macbook

    Benefits:
    - Enforces consistency among products.
    - Easy to switch between product families.
    - Follows the Open/Closed Principle.

    Drawbacks:
    - Can be overkill for simple use cases.
    - Adds more classes and complexity.
"""

# 1. Abstract Product Interfaces

from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class CheckBox(ABC):
    @abstractmethod
    def render(self):
        pass



# 2. Concrete Products

class WindowsButton(Button):
    def render(self):
        return "Creating window's button"

class WindowsCheckBox(CheckBox):
    def render(self):
        return "Creating window's checkbox"


class MacbookButton(Button):
    def render(self):
        return "Creating macbook's button"


class MacbookCheckBox(CheckBox):
    def render(self):
        return "Creating macbook's checkbox"


# 3. Abstract Factory

class GUIAbstractFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox:
        pass


# 4. Concrete Factories

class WindowsGUIFactory(GUIAbstractFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> CheckBox:
        return WindowsCheckBox()

class MacBookGUIFactory(GUIAbstractFactory):
    def create_button(self) -> Button:
        return MacbookButton()

    def create_checkbox(self) -> CheckBox:
        return MacbookCheckBox()


if __name__ == '__main__':
    windows_ui = WindowsGUIFactory()
    print(windows_ui.create_button().render())
    print(windows_ui.create_checkbox().render())

    macbook_ui = MacBookGUIFactory()
    print(macbook_ui.create_button().render())
    print(macbook_ui.create_checkbox().render())
