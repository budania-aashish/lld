"""
    A teacher can teach multiple students
    A students can have multiple teachers
"""

class Teacher:
    def __init__(self, name, subject, students):
        self.name = name
        self.subject = subject
        self.students = []

    def get_name(self):
        return self.name

    def get_details(self):
        print(f"{self.name} teaches {self.subject}")
        print(f"students of {self.name} are : ")
        for student in self.students:
            print(f"{student.get_name()}")
        print("\n")

    def add_student(self, student):
        self.students.append(student)

class Student:
    def __init__(self, name, class_room):
        self.name = name
        self.class_room = class_room
        self.teachers = []

    def get_name(self):
        return self.name

    def get_details(self):
        print(f"{self.name} is in class room {self.class_room}")
        print(f"{self.name} is taught by ")
        for teacher in self.teachers:
            print(f"{teacher.get_name()}")
        print("\n")

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

if __name__ == "__main__":
    student1 = Student("Adam", 6)
    student2 = Student("Rohan", 8)
    student1.get_details()
    student2.get_details()
    teacher1 = Teacher("Gill", "Mathematics", [])
    teacher2 = Teacher("Sarine", "Chemistry", [])
    teacher1.get_details()
    teacher2.get_details()
    teacher1.add_student(student1)
    teacher1.get_details()
    teacher2.add_student(student2)
    teacher2.add_student(student1)
    teacher2.get_details()
    student2.add_teacher(teacher2)
    student2.add_teacher(teacher1)
    student1.add_teacher(teacher1)
    student1.get_details()
    student2.get_details()