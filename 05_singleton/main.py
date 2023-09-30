from .singleton import Singleton


def run() -> None:
    s1 = Singleton()
    s2 = Singleton()
    print(f'Are {s1} and {s2} the same instances? {s1 is s2}')


if __name__ == '__main__':
    run()
