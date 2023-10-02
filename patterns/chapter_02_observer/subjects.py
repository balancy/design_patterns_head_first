"""Abstract class for subject and one concrete implementation.

Subject class aim is to handle observers subscription and notify them about
state changement. WeatherData class is concrete implementation of Subject that
notifies its observers about sensors measures.
"""

from abc import ABC, abstractmethod

from .observers import Observer


class Subject(ABC):
    """Interface for subject which could notify its observers."""

    _observers: list[Observer]

    def register_observer(self, observer: Observer) -> None:
        """Subscribe observer."""
        print(f'Adding observer {observer} to {self}')
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        """Remove osbserver from subscribers."""
        print(f'Removing observer {observer} from {self}')
        self._observers.remove(observer)

    @abstractmethod
    def notify_observers(self) -> None:
        """Abstract method for notifying all observers.

        All child classes should implement this method.
        """
        ...

    def __repr__(self) -> str:
        """Return class name."""
        return self.__class__.__name__


class SubjectWithSensors(Subject):
    """Interface for subject which could set measurements."""

    @abstractmethod
    def set_measurements(self, *args, **kwargs) -> None:
        """Abstract method for setting sensors measurements.

        All child classes should implement this method.
        """
        ...


class WeatherData(SubjectWithSensors):
    """Concrete class implementing SubjectWithSensors interface."""

    def __init__(self) -> None:
        """Initialize observers list."""
        self._observers: list[Observer] = []
        self._temperature: float
        self._humidity: float
        self._pressure: float

    def notify_observers(self) -> None:
        """Notify all observers."""
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def set_measurements(
        self,
        temperature: float,
        humidity: float,
        pressure: float,
    ) -> None:
        """Set new measurements and call its notification method."""
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()
