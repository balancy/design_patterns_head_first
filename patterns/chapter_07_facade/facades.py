"""Home theater (facade to handle all devices) module."""

from .devices import Amplifier, DvdPlayer, Light, Popper, Projector, Screen


class HomeTheaterFacade:
    """Home theater facade class."""

    def __init__(self) -> None:
        """Initialize home theater facade."""
        self._amp: Amplifier = Amplifier()
        self._player: DvdPlayer = DvdPlayer()
        self._light: Light = Light()
        self._popper: Popper = Popper()
        self._projector: Projector = Projector()
        self._screen: Screen = Screen()

    def watch_movie(self) -> None:
        """Watch movie method.

        Incapsulate commands for all devices to watch a movie.
        """
        print('Get ready to watch a movie...')
        print()

        self._popper.turn_on()
        self._popper.pop()

        self._light.turn_on()
        self._light.dim(10)

        self._screen.down()

        self._projector.turn_on()
        self._projector.set_input('DVD')
        self._projector.set_wide_screen_mode()

        self._amp.turn_on()
        self._amp.set_dvd()
        self._amp.set_surround_sound()
        self._amp.set_volume(5)

        self._player.turn_on()
        self._player.play('The Lord of the Rings')

        print('Enjoy the movie!')

    def end_movie(self) -> None:
        """End movie method.

        Incapsulate commands for all devices to end watching a movie.
        """
        print()
        print('Shutting movie theater down...')
        print()

        self._popper.turn_off()
        self._light.turn_off()
        self._screen.up()
        self._projector.turn_off()
        self._amp.turn_off()
        self._player.turn_off()

        print('Movie theater is closed')
