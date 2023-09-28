from .interfaces import DisplayElement, Observer


class ConditionsDisplay(Observer, DisplayElement):
    def update(
        self,
        temperature: float,
        humidity: float,
        pressure: float,
    ) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self.display()

    def display(self) -> None:
        print(
            f'Current conditions: {self._temperature}F degrees '
            f'and {self._humidity}% humidity'
        )


class StatisticsDisplay(Observer, DisplayElement):
    def update(
        self,
        temperature: float,
        humidity: float,
        pressure: float,
    ) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.display()

    def display(self) -> None:
        print(
            f'Current statistics: {self._temperature}F degrees, '
            f'{self._humidity}% humidity and {self._pressure} pressure'
        )
