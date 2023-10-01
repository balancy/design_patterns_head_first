class Popper:
    def turn_on(self) -> None:
        print('Pop-corn: popping')

    def pop(self) -> None:
        print('Pop-corn: poped')

    def turn_off(self) -> None:
        print('Pop-corn: off')


class Light:
    def turn_on(self) -> None:
        print('Light: turned on')

    def dim(self, value: int) -> None:
        print(f'Light: dimmed to {value}')

    def turn_off(self) -> None:
        print('Light: turned off')


class Screen:
    def down(self) -> None:
        print('Screen: is down')

    def up(self) -> None:
        print('Screen: is up')


class Projector:
    def turn_on(self) -> None:
        print('Projector: turned on')

    def set_input(self, input_value: str) -> None:
        print(f'Projector: input set to {input_value}')

    def set_wide_screen_mode(self) -> None:
        print('Projector: switched to wide screen mode')

    def turn_off(self) -> None:
        print('Projector: turned off')


class Amplifier:
    def turn_on(self) -> None:
        print('Amplifier: turned on')

    def set_dvd(self) -> None:
        print('Amplifier: DVD is set')

    def set_surround_sound(self) -> None:
        print('Amplifier: surround sound is set')

    def set_volume(self, value: int) -> None:
        print(f'Amplifier: volume is set to {value}')

    def turn_off(self) -> None:
        print('Amplifier: turned off')


class DvdPlayer:
    def turn_on(self) -> None:
        print('DVD: turned on')

    def play(self, movie: str) -> None:
        print(f'DVD: playing {movie}')

    def turn_off(self) -> None:
        print('DVD: turned off')
