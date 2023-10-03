"""Module for testing pattern "Command"."""


import pytest

from patterns.chapter_06_command.commands import (
    Command,
    TurnDeviceOffCommand,
    TurnDeviceOnCommand,
)
from patterns.chapter_06_command.invokers import Invoker
from patterns.chapter_06_command.receivers import (
    TV,
    BedroomLight,
    Device,
    KitchenLight,
)

pytestmark = pytest.mark.parametrize(
    ('command', 'receiver', 'expected_receiver_status'),
    [
        (TurnDeviceOnCommand, KitchenLight(), True),
        (TurnDeviceOffCommand, KitchenLight(), False),
        (TurnDeviceOnCommand, BedroomLight(), True),
        (TurnDeviceOffCommand, TV(), False),
    ],
)


def test_set_command(
    command: type[Command],
    receiver: Device,
    expected_receiver_status: bool,
) -> None:
    """Test set command pattern.

    Commands set by Invoker should change status of Receiver.
    """
    remote_control: Invoker = Invoker()

    remote_control.set_command(command(receiver))
    remote_control.execute_command()

    assert receiver.is_on == expected_receiver_status
