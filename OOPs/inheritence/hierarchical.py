class ProjectOwner:
    def __init__(self, name):
        self.name = name

    def manage(self):
        print("{0} manages the project".format(self.name))

class QA(ProjectOwner):
    def quality_assurance(self):
        print("{0} assures the quality of the project".format(self.name))

class Dev(ProjectOwner):
    def develop_functionality(self):
        print("{0} develops the functionality of the project".format(self.name))


if __name__ == '__main__':
    manager = ProjectOwner("Rahul")
    manager.manage()

    qa = QA("Amit")
    qa.quality_assurance()
    qa.manage()

    dev = Dev("Praveen")
    dev.develop_functionality()
    dev.manage()

