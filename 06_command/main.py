from collections import deque

from .commands import Command, TurnDeviceOffCommand, TurnDeviceOnCommand
from .invokers import Invoker
from .receivers import TV, BedroomLight, KitchenLight, Receiver


def run() -> None:
    bedroom_light: Receiver = BedroomLight()
    kitchen_light: Receiver = KitchenLight()
    tv: Receiver = TV()

    commands: deque[Command] = deque(
        [
            TurnDeviceOnCommand(bedroom_light),
            TurnDeviceOnCommand(kitchen_light),
            TurnDeviceOffCommand(kitchen_light),
            TurnDeviceOnCommand(tv),
        ]
    )

    auto_remote_control: Invoker = Invoker()

    # executing sentence of commands
    auto_remote_control.set_commands(commands)

    for _ in range(len(commands)):
        auto_remote_control.execute_command()
        print('-' * 20)

    # trying to undo and reexecute the last command
    auto_remote_control.undo_command()
    print('-' * 20)

    auto_remote_control.execute_command()


if __name__ == '__main__':
    run()
