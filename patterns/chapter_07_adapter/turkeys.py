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

    _sound_produced: str = 'Gobble gobble'
    _flying_behaviour: str = 'I\'m flying a short distance'

    def gobble(self) -> None:
        """Gobble method implementation."""
        print(self._sound_produced)

    def short_fly(self) -> None:
        """Short fly method implementation."""
        print(self._flying_behaviour)

    @property
    def sound_produced(self) -> str:
        """Return produced sound."""
        return self._sound_produced

    @property
    def flying_behaviour(self) -> str:
        """Return flying behaviour."""
        return self._flying_behaviour
