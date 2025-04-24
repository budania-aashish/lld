class Singleton:
    __instance = None

    @staticmethod
    def get_instance_singleton():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if self.__instance is not None:
            raise Exception("Singleton class already exists") # to avoid multiple time creation
        else:
            Singleton.__instance = self

if __name__ == '__main__':
    s1 = Singleton.get_instance_singleton()
    s2 = Singleton.get_instance_singleton()

    print(s1 == s2)