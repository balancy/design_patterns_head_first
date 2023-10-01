from abc import ABC, abstractmethod

from .receivers import Receiver


class Command(ABC):
    def __init__(self, receiver: Receiver) -> None:
        self._receiver = receiver

    @abstractmethod
    def execute(self) -> None:
        ...

    @abstractmethod
    def undo(self) -> None:
        ...

    def __repr__(self) -> str:
        return self.__class__.__name__


class TurnDeviceOnCommand(Command):
    def execute(self) -> None:
        print(f'Executing "{self._receiver}" turning on.')
        self._receiver.on()

    def undo(self) -> None:
        print(f'Undoing "{self._receiver}" turning on.')
        self._receiver.off()


class TurnDeviceOffCommand(Command):
    def execute(self) -> None:
        print(f'Executing "{self._receiver}" turning off.')
        self._receiver.off()

    def undo(self) -> None:
        print(f'Undoing "{self._receiver}" turning off.')
        self._receiver.on()
