"""One abstract turkey class and one class implementing it."""

from abc import ABC, abstractmethod


class Turkey(ABC):
    """Abstract turkey class."""

    @abstractmethod
    def gobble(self) -> None:
        """Abstract gobble method.

        All child classes should implement it.
        """
        ...

    @abstractmethod
    def short_fly(self) -> None:
        """Abstract short fly method.

        All child classes should implement it.
        """
        ...


class WildTurkey(Turkey):
    """Wild turkey class implementing abstract turkey class."""

    def gobble(self) -> None:
        """Gobble method implementation."""
        print('Gobble gobble')

    def short_fly(self) -> None:
        """Short fly method implementation."""
        print('I\'m flying a short distance')
