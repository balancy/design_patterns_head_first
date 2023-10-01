from abc import ABC, abstractmethod


class Turkey(ABC):
    @abstractmethod
    def gobble(self) -> None:
        ...

    @abstractmethod
    def short_fly(self) -> None:
        ...


class WildTurkey(Turkey):
    def gobble(self) -> None:
        print('Gobble gobble')

    def short_fly(self) -> None:
        print('I\'m flying a short distance')
