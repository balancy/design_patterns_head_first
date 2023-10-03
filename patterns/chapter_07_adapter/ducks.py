"""One abstract duck class and one class implementing it."""

from abc import ABC, abstractmethod


class Duck(ABC):
    """Abstract duck class."""

    @abstractmethod
    def quack(self) -> None:
        """Abstract quack method.

        All child classes should implement it.
        """
        ...

    @abstractmethod
    def fly(self) -> None:
        """Abstract fly method.

        All child classes should implement it.
        """
        ...


class MallardDuck(Duck):
    """Mallard duck class implementing abstract duck class."""

    def quack(self) -> None:
        """Quack method implementation."""
        print('Quack')

    def fly(self) -> None:
        """Fly method implementation."""
        print('I\'m flying')
