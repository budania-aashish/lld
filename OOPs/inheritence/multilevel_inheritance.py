class LivingEntity:
    def __init__(self, name):
        self.name = name

    def has_life(self):
        print("{0} has a life".format(self.name))

class Animal(LivingEntity):
    def lives_in_forest(self):
        print("{0} lives in forest".format(self.name))


class Dog(Animal):
    def barks(self):
        print("{0} dog barks".format(self.name))


class Person(LivingEntity):
    def lives_in_city(self):
        print("{0} lives in city".format(self.name))

class Adult(Person):
    def has_age(self):
        print("{0} has age > 18".format(self.name))

if __name__ == '__main__':
    dog = Dog("Tommy")
    dog.barks()
    dog.lives_in_forest()
    dog.has_life()

    man = Adult("Aashish")
    man.has_life()
    man.has_age()
    man.lives_in_city()
