"""
    Purpose: Notify multiple objects about state changes.

"""

class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, msg):
        for obs in self.observers:
            obs.update(msg)

class Observer:
    def update(self, msg):
        print(f"Received: {msg}")

if __name__ == '__main__':
    # Usage
    subject = Subject()
    subject.subscribe(Observer())
    subject.notify("Hello Observers!")

"""
    Pros:
    - Loose coupling.
    - Dynamic notification.
    
    Cons:
    - Can be hard to debug.
    - Many observers = more complexity.
"""