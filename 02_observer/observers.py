from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float) -> None:
        ...

    def __repr__(self) -> str:
        return self.__class__.__name__


class DisplayElement(ABC):
    @abstractmethod
    def display(self) -> None:
        ...


class ConditionsDisplay(Observer, DisplayElement):
    def update(self, temp: float, humidity: float, pressure: float) -> None:
        self._temperature = temp
        self._humidity = humidity
        self.display()

    def display(self) -> None:
        print(
            f'Current conditions: {self._temperature}F degrees '
            f'and {self._humidity}% humidity'
        )


class StatisticsDisplay(Observer, DisplayElement):
    def update(self, temp: float, humidity: float, pressure: float) -> None:
        self._temperature = temp
        self._humidity = humidity
        self._pressure = pressure
        self.display()

    def display(self) -> None:
        print(
            f'Current statistics: {self._temperature}F degrees, '
            f'{self._humidity}% humidity and {self._pressure} pressure'
        )
