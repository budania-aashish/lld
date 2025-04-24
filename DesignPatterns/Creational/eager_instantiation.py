class Singleton:
    __instance = None

    def __init__(self):
        if self.__instance is not None:
            raise Exception("Singleton instance already exists")
        Singleton.__instance = self

    @staticmethod
    def get_instance():
        return Singleton.__instance

# Eager instantiation, while loading the class
Singleton()