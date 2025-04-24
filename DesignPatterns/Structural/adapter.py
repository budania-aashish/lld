"""
    The Adapter Pattern allows objects with incompatible interfaces to work together
    by wrapping one object with an interface expected by the client.

    Benefits
    - Allows reusability of existing code without modifying it.
    - Promotes flexibility and maintainability.

    Drawbacks
    - Adds extra layer of abstraction (which may slightly increase complexity).
    - Not always efficient for performance-critical paths.

"""

from abc import ABC, abstractmethod

class OldPrinter(ABC):
    @abstractmethod
    def print_text(self, text):
        pass

class OldPrinterClass(OldPrinter):
    def print_text(self, text):
        print(f"text printed via old printer : {text}")


class NewPrinter(ABC):
    @abstractmethod
    def output(self, message):
        pass


class NewPrinterClass(NewPrinter):
    def output(self, message):
        print(f"text output via a new printer : {message}")


class PrintAdapter:
    def __init__(self, new_printer_obj):
        self.new_printer = new_printer_obj

    def print_text(self, text):
        self.new_printer.output(text)

# client code
if __name__ == '__main__':
    old_printer = OldPrinterClass()
    old_printer.print_text("Hello!")
    new_printer = NewPrinterClass()
    new_printer.output("Hello!")
    print_adapter = PrintAdapter(NewPrinterClass())
    print_adapter.print_text("Hello!")