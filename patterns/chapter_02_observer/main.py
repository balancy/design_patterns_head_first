"""Main entrypoint module for observer pattern."""

from .observers import ConditionsDisplay, Observer, StatisticsDisplay
from .subjects import SubjectWithSensors, WeatherData


def set_sensors_measurements(
    subject: SubjectWithSensors,
    measurements: tuple[float, float, float],
) -> None:
    """Set sensors measurements for subject."""
    subject.set_measurements(*measurements)


def test_drive() -> None:
    """Interacting weather data station and two observers."""
    weather_station: SubjectWithSensors = WeatherData()
    conditions_display: Observer = ConditionsDisplay()
    statistics_display: Observer = StatisticsDisplay()

    for display in (conditions_display, statistics_display):
        weather_station.register_observer(display)

    measurements = [
        (80, 65, 30.4),
        (82, 70, 29.2),
        (78, 90, 29.2),
    ]

    for measurement in measurements:
        set_sensors_measurements(weather_station, measurement)

    weather_station.remove_observer(statistics_display)
    set_sensors_measurements(weather_station, (62, 90, 28.1))


if __name__ == '__main__':
    test_drive()
