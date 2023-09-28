from .observers import ConditionsDisplay, Observer, StatisticsDisplay
from .subjects import Subject, WeatherData


def run() -> None:
    weather_station: Subject = WeatherData()
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
        weather_station.set_measurements(*measurement)

    weather_station.remove_observer(statistics_display)
    weather_station.set_measurements(62, 90, 28.1)


if __name__ == '__main__':
    run()
