"""Abstract class for fly behaviour and two concrete implementations."""

from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    """Interface for fly behavior."""

    @abstractmethod
    def perform_fly(self) -> None:
        """Perform fly behavior.

        All child classes should implement this method.
        """
        ...


class FlyWithWings(FlyBehavior):
    """Fly behavior implementation for ducks with wings."""

    def perform_fly(self) -> None:
        """Perform fly behavior."""
        print('I\'m flying!')


class FlyNoWay(FlyBehavior):
    """Fly behavior implementation for ducks without wings."""

    def perform_fly(self) -> None:
        """Perform fly behavior."""
        print('I can\'t fly')
