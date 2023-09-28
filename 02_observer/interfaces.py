from __future__ import annotations

from abc import ABC, abstractmethod


class Subject:
    def __init__(self) -> None:
        self._observers: list[Observer] = []
        self._temperature: float
        self._humidity: float
        self._pressure: float

    def register_observer(self, observer: Observer) -> None:
        print(f'Adding observer {observer} to {self}')
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        print(f'Removing observer {observer} from {self}')
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def __repr__(self) -> str:
        return self.__class__.__name__


class Observer(ABC):
    @abstractmethod
    def update(
        self,
        temperature: float,
        humidity: float,
        pressure: float,
    ) -> None:
        pass

    def __repr__(self) -> str:
        return f'Observer {self.__class__.__name__}'


class DisplayElement(ABC):
    @abstractmethod
    def display(self, subject: 'Subject') -> None:
        pass
        pass
        pass
