"""Devices module."""


class Popper:
    """Popper device class."""

    def turn_on(self) -> None:
        """Turn on popper."""
        print('Pop-corn: popping')

    def pop(self) -> None:
        """Pop pop-corn."""
        print('Pop-corn: poped')

    def turn_off(self) -> None:
        """Turn off popper."""
        print('Pop-corn: off')


class Light:
    """Light device class."""

    def turn_on(self) -> None:
        """Turn on light."""
        print('Light: turned on')

    def dim(self, value: int) -> None:
        """Dim light."""
        print(f'Light: dimmed to {value}')

    def turn_off(self) -> None:
        """Turn off light."""
        print('Light: turned off')


class Screen:
    """Screen device class."""

    def down(self) -> None:
        """Move screen down."""
        print('Screen: is down')

    def up(self) -> None:
        """Move screen up."""
        print('Screen: is up')


class Projector:
    """Projector device class."""

    def turn_on(self) -> None:
        """Turn on projector."""
        print('Projector: turned on')

    def set_input(self, input_value: str) -> None:
        """Set input device for projector."""
        print(f'Projector: input set to {input_value}')

    def set_wide_screen_mode(self) -> None:
        """Set wide screen mode for projector."""
        print('Projector: switched to wide screen mode')

    def turn_off(self) -> None:
        """Turn off projector."""
        print('Projector: turned off')


class Amplifier:
    """Amplifier device class."""

    def turn_on(self) -> None:
        """Turn on amplifier."""
        print('Amplifier: turned on')

    def set_dvd(self) -> None:
        """Set DVD for amplifier."""
        print('Amplifier: DVD is set')

    def set_surround_sound(self) -> None:
        """Set surround sound for amplifier."""
        print('Amplifier: surround sound is set')

    def set_volume(self, value: int) -> None:
        """Set volume for amplifier."""
        print(f'Amplifier: volume is set to {value}')

    def turn_off(self) -> None:
        """Turn off amplifier."""
        print('Amplifier: turned off')


class DvdPlayer:
    """DVD player device class."""

    def turn_on(self) -> None:
        """Turn on DVD player."""
        print('DVD: turned on')

    def play(self, movie: str) -> None:
        """Play movie on DVD player."""
        print(f'DVD: playing {movie}')

    def turn_off(self) -> None:
        """Turn off DVD player."""
        print('DVD: turned off')
