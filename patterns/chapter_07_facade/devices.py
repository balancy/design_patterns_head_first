"""Devices module."""


class Device:
    """Device base class."""

    def __init__(self) -> None:
        """Initialize device."""
        self._is_on: bool = False
        print(f'{self.__class__.__name__} is on')

    def turn_on(self) -> None:
        """Turn on device."""
        self._is_on = True
        print(f'{self.__class__.__name__} is on')

    def turn_off(self) -> None:
        """Turn off device."""
        self._is_on = False
        print(f'{self.__class__.__name__} is off')

    @property
    def is_on(self) -> bool:
        """Check if device is on."""
        return self._is_on


class Popper(Device):
    """Popper device class."""

    def pop(self) -> None:
        """Pop pop-corn."""
        print('Pop-corn: poped')


class Light(Device):
    """Light device class."""

    def dim(self, value: int) -> None:
        """Dim light."""
        print(f'Light: dimmed to {value}')


class Screen(Device):
    """Screen device class."""

    def down(self) -> None:
        """Move screen down."""
        print('Screen: is down')

    def up(self) -> None:
        """Move screen up."""
        print('Screen: is up')


class Projector(Device):
    """Projector device class."""

    def set_input(self, input_value: str) -> None:
        """Set input device for projector."""
        print(f'Projector: input set to {input_value}')

    def set_wide_screen_mode(self) -> None:
        """Set wide screen mode for projector."""
        print('Projector: switched to wide screen mode')


class Amplifier(Device):
    """Amplifier device class."""

    def set_dvd(self) -> None:
        """Set DVD for amplifier."""
        print('Amplifier: DVD is set')

    def set_surround_sound(self) -> None:
        """Set surround sound for amplifier."""
        print('Amplifier: surround sound is set')

    def set_volume(self, value: int) -> None:
        """Set volume for amplifier."""
        print(f'Amplifier: volume is set to {value}')


class DvdPlayer(Device):
    """DVD player device class."""

    def play(self, movie: str) -> None:
        """Play movie on DVD player."""
        print(f'DVD: playing {movie}')
