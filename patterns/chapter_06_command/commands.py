"""Abstract base command class and two implementations."""

from abc import ABC, abstractmethod

from .receivers import Receiver


class Command(ABC):
    """Abstract base command class."""

    def __init__(self, receiver: Receiver) -> None:
        """Initialize with a receiver instance."""
        self._receiver = receiver

    @abstractmethod
    def execute(self) -> None:
        """Execute the command."""
        ...

    @abstractmethod
    def undo(self) -> None:
        """Undo the command."""
        ...

    def __repr__(self) -> str:
        """Return the command representation."""
        return self.__class__.__name__


class TurnDeviceOnCommand(Command):
    """Abstract command class implementation.

    Command is reponsible for turning device on.
    """

    def execute(self) -> None:
        """Execute the command."""
        print(f'Executing "{self._receiver}" turning on.')
        self._receiver.on()

    def undo(self) -> None:
        """Undo the command."""
        print(f'Undoing "{self._receiver}" turning on.')
        self._receiver.off()


class TurnDeviceOffCommand(Command):
    """Abstract command class implementation.

    Command is reponsible for turning device off.
    """

    def execute(self) -> None:
        """Execute the command."""
        print(f'Executing "{self._receiver}" turning off.')
        self._receiver.off()

    def undo(self) -> None:
        """Undo the command."""
        print(f'Undoing "{self._receiver}" turning off.')
        self._receiver.on()
