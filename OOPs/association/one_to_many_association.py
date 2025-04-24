"""
    one school has many students [one->many]
"""

class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def get_details(self):
        print(f"School Name : {school.name}")
        print(f"students of school are: ")
        for student in self.students:
            student.get_details()
        print("\n")

    def add_student(self, student):
        self.students.append(student)

    def get_name(self):
        return self.name

class Student:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        print(f"student name : {self.name}")

if __name__ == '__main__':
    school = School("Central Academy", [])
    school.get_details()
    student1 = Student("Adam")
    student2 = Student("Chris")
    student2.get_details()
    student1.get_details()
    school.add_student(student1)
    school.get_details()
    school.add_student(student2)
    school.get_details()