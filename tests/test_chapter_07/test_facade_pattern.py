"""Module for testing pattern "Facade"."""


import pytest

from patterns.chapter_07_facade.facades import HomeTheaterFacade

pytestmark = pytest.mark.parametrize(
    ('method_name', 'are_devices_on'),
    [
        ('watch_movie', True),
        ('end_movie', False),
    ],
)


def test_facade_pattern(method_name: str, are_devices_on: bool) -> None:
    """Test facade pattern.

    Calling one method of facade class should call all incapsulated methods.
    """
    home_theater: HomeTheaterFacade = HomeTheaterFacade()
    called_method = getattr(HomeTheaterFacade, method_name)

    called_method(home_theater)

    assert are_devices_on == all(
        device.is_on for device in home_theater.handled_devices
    )
