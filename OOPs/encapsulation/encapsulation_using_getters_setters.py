class Employee:
    def __init__(self):
        self.__name = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name
        print(f"Set name {self.__name}")

    def set_age(self, age):
        if age<18:
            print(f"Age must be greater than 18")
            return 
        self.__age = age
        print(f"Set age {self.__age}")

    def get_name(self):
        print(f"Name of the employee is {self.__name}")

    def get_age(self):
        print(f"Age of the employee is {self.__age}")

    def get_details(self):
        print(f"Employee Name : {self.__name}, Employee Age : {self.__age}")



if __name__ == '__main__':
    e1 = Employee()
    e1.set_name("Adam")
    e1.set_age(49)
    e1.get_name()
    e1.get_age()
    e1.get_details()
    e1 = Employee()
    e1.set_name("Mark")
    e1.set_age(6)
    e1.get_name()
    e1.get_age()
    e1.get_details()
