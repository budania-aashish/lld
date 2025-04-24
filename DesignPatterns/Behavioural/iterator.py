"""
    Purpose: Traverse a collection without exposing its internal structure.
"""

class Numbers:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def __iter__(self):
        return iter(self.nums)


if __name__ == '__main__':
    # Usage
    for num in Numbers():
        print(num)
"""
    Pros:
    - Simplifies traversal.
    - Hides collection internals.

    Cons:
    - Adds extra classes if custom iterator needed.
"""

