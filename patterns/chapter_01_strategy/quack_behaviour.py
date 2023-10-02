"""Abstract class for quack behaviour and three concrete implementations."""

from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    """Interface for quack behavior."""

    @abstractmethod
    def perform_quack(self) -> None:
        """Perform quack behavior.

        All child classes should implement this method.
        """
        ...


class Quack(QuackBehavior):
    """Quack behavior implementation for somebody quacking."""

    def perform_quack(self) -> None:
        """Perform quack behavior."""
        print('Quack')


class MuteQuack(QuackBehavior):
    """Quack behavior implementation for somebody silent."""

    def perform_quack(self) -> None:
        """Perform quack behavior."""
        print('<< Silence >>')


class Squeak(QuackBehavior):
    """Quack behavior implementation for somebody squeaking."""

    def perform_quack(self) -> None:
        """Perform quack behavior."""
        print('Squeak')
