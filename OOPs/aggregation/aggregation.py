"""
    Aggregation: One of the important topic in OOPs, represents a Has-A relationship
    between two classes, but with a crucial distinction - the lifecycle of the contained
    object is independent of the container object.

    This means while that while one class contains another class, the contained object
    can exist independently of the container.

    Aggregation allows for better code modularity, code reuse and maintainability.
    It's different from Composition where contained object can't exist without container.

    This means if the container object is destroyed, contained object can be used anywhere
    in the application.

    Key Characteristics of Aggregation:
    - Represents a Has-A relationship
    - The container object can exist independently of the container
    - Implemented using reference of the objects
    - Promotes loose coupling between objects

"""

class Professor:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teaches(self):
        print(f"Professor {self.name} teaches {self.subject}")

    def get_details(self):
        print(f"Professor Name : {self.name}, Subject : {self.subject}")

class University:
    def __init__(self, name, location, professors):
        self.name = name
        self.location = location
        self.professors = professors

    def add_professors(self, professor):
        self.professors.append(professor)

    def get_details(self):
        print(f"University {self.name}, situated in {self.location}")
        for professor in self.professors:
            professor.get_details()


if __name__ == '__main__':
    prof1 = Professor("Dr John", "Physics")
    prof2 = Professor("Dr Smith", "Chemistry")
    prof1.teaches()
    prof2.teaches()
    university = University("Delhi University", "Delhi", [])
    university.get_details()
    university.add_professors(prof1)
    university.get_details()
    university.add_professors(prof2)
    university.get_details()
