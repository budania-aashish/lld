"""
    Purpose: Switch between algorithms at runtime.
"""

class StrategyAdd:
    def execute(self, a, b):
        return a + b

class StrategyMultiply:
    def execute(self, a, b):
        return a * b

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def do_operation(self, a, b):
        return self.strategy.execute(a, b)

if __name__ == '__main__':
    # Usage
    context = Context(StrategyAdd())
    print(context.do_operation(2, 3))  # 5

    context.strategy = StrategyMultiply()
    print(context.do_operation(2, 3))  # 6

"""
    Pros:
    - Easy to swap algorithms.
    - Cleaner code.

    Cons:
    - More classes.
    - Strategy selection is manual.
"""