from .interfaces import Subject


class WeatherData(Subject):
    def set_measurements(
        self,
        temperature: float,
        humidity: float,
        pressure: float,
    ) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.measurements_changed()

    def measurements_changed(self) -> None:
        self.notify_observers()
