"""Module for testing pattern "Strategy"."""


import random

import pytest

from patterns.chapter_02_observer.main import set_sensors_measurements
from patterns.chapter_02_observer.observers import Observer, StatisticsDisplay
from patterns.chapter_02_observer.subjects import (
    SubjectWithSensors,
    WeatherData,
)


@pytest.fixture()
def random_measurements() -> tuple[float, float, float]:
    """Fixture for generating random measurements."""
    return (
        random.uniform(0, 100),
        random.uniform(0, 100),
        random.uniform(0, 100),
    )


def test_pattern_as_black_box(
    capsys,
    random_measurements: tuple[float, float, float],
) -> None:
    """Test pattern as black box."""
    weather_station: SubjectWithSensors = WeatherData()
    statistics_display: Observer = StatisticsDisplay()
    weather_station.register_observer(statistics_display)

    set_sensors_measurements(weather_station, random_measurements)
    captured = capsys.readouterr()

    for measurement in random_measurements:
        assert str(measurement) in captured.out
