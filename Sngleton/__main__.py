from threading import Thread, Lock


class SingletonMethod(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = instance
        return cls.__instances[cls]


class SingletonMethodThread(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance

        return cls._instances[cls]


class Singleton(metaclass=SingletonMethod):
    pass


class SingletonThread(metaclass=SingletonMethodThread):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value


def test_singleton():
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton Done")
    else:
        print("Singleton Failed")


def singleton_thread(value: str) -> None:
    singleton = SingletonThread(value)
    print(singleton.value)


def test_singleton_thread():
    process1 = Thread(target=singleton_thread, args=("First",))
    process2 = Thread(target=singleton_thread, args=("Second",))
    process1.start()
    process2.start()


if __name__ == "__main__":
    test_singleton()
    test_singleton_thread()
