"""
    multiple inheritance is also possible in python unlike java
"""

class Employee:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print("Hi {0}! you are welcome!".format(self.name))
        #  not an error this gets printed if used first as Developer(Employee, BuildingAccess)

class BuildingAccess:
    def __init__(self, name):
        self.name = name

    def access_canteen(self):
        print("{0} can access the canteen".format(self.name))

    def welcome(self):
        print("Hi {0}! you are welcome!!!".format(self.name))
        # not an error, this gets printed if used first as Developer(BuildingAccess, Employee)

class Developer(BuildingAccess, Employee):
    def develops_software(self):
        print('{0} develops software'.format(self.name))

if __name__ == '__main__':
    dev = Developer("Adam")
    dev.welcome()
    dev.access_canteen()





