from .abstract_factory.test_drive import run as abstract_factory_run
from .factory_method.test_drive import run as factory_method_run


def main() -> None:
    print('-' * 20)
    print('Factory Method Pattern')
    factory_method_run()

    print('-' * 20)
    print('Abstract Factory Pattern')
    abstract_factory_run()


if __name__ == '__main__':
    main()
