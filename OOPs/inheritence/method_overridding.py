class Animal:
    def __init__(self, name):
        self.name = name

    def eats(self):
        print('{0} eats'.format(self.name))

class Dog(Animal):
    def eats(self):
        print('{0} eats veg and non-veg'.format(self.name))

if __name__ == '__main__':
    dog = Dog("Tommy")
    dog.eats()

