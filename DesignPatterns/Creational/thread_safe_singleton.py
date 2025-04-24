import threading

class Singleton:
    __instance = None
    __lock = threading.Lock()
    @staticmethod
    def get_singleton_instance():
        if Singleton.__instance is None:
            with Singleton.__lock:
                if Singleton.__instance is None:
                    Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("Singleton object already exists")
        else:
            Singleton.__instance = self

if __name__ == '__main__':
    s1 = Singleton.get_singleton_instance()
    s2 = Singleton.get_singleton_instance()
    print(s1==s2)