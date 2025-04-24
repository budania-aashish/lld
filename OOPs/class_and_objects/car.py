"""
    class: class is a blueprint of template
    that defines the attributes(fields)
    and behaviours(methods/functions)
    of an object.

    We can say object is a real entity and
    class is just a representation of that entity

    To define class we use a class keyboard
"""

class Car:
    # constructor of the class
    def __init__(self, color, make, model, year):
        self.color = color
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print('color is {0}'.format(self.color))
        print('make is {0}'.format(self.make))
        print('model is {0}'.format(self.model))
        print('year is {0}'.format(self.year))


"""
    object : an object is an instance of the class. 
    
    When we create an instance of class, it brings 
    the blueprint to the existence. 
    
    This blueprint consists of states and behaviours
    defined by the class. The states basically represent 
    the attributes/fields and behaviours consist of 
    methods/functions.
    
    Each object holding its own copy of the data  
    
    To create an object you can call the class constructor. 
"""


car1 = Car("white", "toyota", "corolla", "2015")
car2 = Car("gray", "honda", "amaze", "2024")


car1.display_details()
car2.display_details()
