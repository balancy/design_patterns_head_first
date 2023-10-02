"""Abstract class for observer and two concrete implementations."""

from abc import ABC, abstractmethod


class Observer(ABC):
    """Interface for observer."""

    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float) -> None:
        """Abstract update method.

        All child classes should implement this method.
        """
        ...

    def __repr__(self) -> str:
        """Return class name."""
        return self.__class__.__name__


class DisplayElement(ABC):
    """Interface for classes implementing display method."""

    @abstractmethod
    def display(self) -> None:
        """Abstract display method.

        All child classes should implement this method.
        """
        ...


class ConditionsDisplay(Observer, DisplayElement):
    """Concrete class implementing Observer and DisplayElement interface."""

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        """Update temperature and humidity."""
        self._temperature = temp
        self._humidity = humidity
        self.display()

    def display(self) -> None:
        """Display current temperature and humidity."""
        print(
            f'Current conditions: {self._temperature}F degrees '
            f'and {self._humidity}% humidity'
        )


class StatisticsDisplay(Observer, DisplayElement):
    """Concrete class implementing Observer and DisplayElement interface."""

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        """Update temperature, humidity and pressure."""
        self._temperature = temp
        self._humidity = humidity
        self._pressure = pressure
        self.display()

    def display(self) -> None:
        """Display current temperature, humidity and pressure."""
        print(
            f'Current statistics: {self._temperature}F degrees, '
            f'{self._humidity}% humidity and {self._pressure} pressure'
        )
