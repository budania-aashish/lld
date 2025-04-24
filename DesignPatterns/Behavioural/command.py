"""
    Purpose: Encapsulate a request as an object.
"""

class Light:
    def turn_on(self):
        print("Light ON")

class Command:
    def execute(self):
        pass

class TurnOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

if __name__ == '__main__':
    # Usage
    light = Light()
    cmd = TurnOnCommand(light)
    cmd.execute()


"""
    Pros:
    - Decouples sender/receiver.
    - Supports undo/redo.

    Cons:
    - Adds complexity.
"""