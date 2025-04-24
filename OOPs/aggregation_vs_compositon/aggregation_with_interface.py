"""
    when to use aggregation -
    - when an object can independently exist from the container
    - while designing loosely coupled systems
    - When different objects needs to be store across multiple containers
    - While following SOLID particularly the dependency inversion principle (DIP)
"""

from abc import ABC, abstractmethod

class Teachable(ABC):
    @abstractmethod
    def teach(self):
        pass

class Professor(Teachable):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        print(f"Professor {self.name} teaches {self.subject}")

class University:
    def __init__(self, name):
        self.name = name
        self.professors = []

    def add_professor(self, professor):
        self.professors.append(professor)

    def get_details(self):
        print(f"At university {self.name}")
        for professor in self.professors:
            professor.teach()

if __name__ == '__main__':
    university = University("Delhi University")
    university.get_details()
    prof1 = Professor("Mr. Gandhi", "Hindi")
    prof2 = Professor("Mr. Paul", "English")
    university.add_professor(prof1)
    university.add_professor(prof2)
    university.get_details()


