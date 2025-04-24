class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"{name} has salary of {salary}")

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
        print(f"manager has bonus of : {bonus}")

if __name__ == '__main__':
    manager = Manager("Adam", 50000, 1000)
