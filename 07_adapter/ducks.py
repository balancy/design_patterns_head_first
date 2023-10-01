from abc import ABC, abstractmethod


class Duck(ABC):
    @abstractmethod
    def quack(self) -> None:
        ...

    @abstractmethod
    def fly(self) -> None:
        ...


class MallardDuck(Duck):
    def quack(self) -> None:
        print('Quack')

    def fly(self) -> None:
        print('I\'m flying')
