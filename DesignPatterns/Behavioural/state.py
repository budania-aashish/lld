"""
    Purpose: Change behavior based on internal state.
"""

class State:
    def handle(self):
        pass

class Happy(State):
    def handle(self):
        print("I'm happy 😊")

class Sad(State):
    def handle(self):
        print("I'm sad 😢")

class Person:
    def __init__(self, state):
        self.state = state

    def act(self):
        self.state.handle()

if __name__ == '__main__':
    # Usage
    person = Person(Happy())
    person.act()

    person.state = Sad()
    person.act()
