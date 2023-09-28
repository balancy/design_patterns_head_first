from .observers import Observer


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


class WeatherData(Subject):
    def set_measurements(
        self,
        temp: float,
        humidity: float,
        pressure: float,
    ) -> None:
        self._temperature = temp
        self._humidity = humidity
        self._pressure = pressure
        self.measurements_changed()

    def measurements_changed(self) -> None:
        self.notify_observers()
