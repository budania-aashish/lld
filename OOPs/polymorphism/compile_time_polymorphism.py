"""
    Method Overloading

    Unlike C++ or Java, python doesn't provide method overloading.

    We can use the default params or *args to achieve the same functionalities

"""
class MathOperations:
    def __init__(self):
        self.sum = 0

    def add_few_numbers(self, a, b, c=0, d=0):
        self.sum = a+b+c+d
        print(f"sum : {self.sum}")

class AddAll:
    def __init__(self):
        self.total = 0

    def add_all(self, *args):
        self.total = 0
        for val in args:
            self.total+=val
        print(f'sum: {self.total}')


if __name__ == '__main__':
    math_operations = MathOperations()
    math_operations.add_few_numbers(2,3)
    math_operations.add_few_numbers(2, 3, 4)
    math_operations.add_few_numbers(2, 3, 4, 5)

    add_values = AddAll()
    add_values.add_all(1)
    add_values.add_all(1,2,3)
    add_values.add_all(1,2,3,4,5,6)
"""
    why default args : to support method overloading and keeping value optional doesn't affect the functionality
    reduces redundancy : by using a single method for similar operations 
"""

    
