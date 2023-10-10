"""Module for testing pattern "State"."""


import pytest

from patterns.chapter_10_state.gumball_machine import GumballMachine
from patterns.chapter_10_state.state import (
    HasQuarterState,
    NoQuarterState,
    SoldOutState,
    SoldState,
    State,
)

pytestmark = pytest.mark.parametrize(
    ('initial_state', 'gumballs_amount', 'action', 'new_state'),
    [
        (NoQuarterState(), 2, 'insert_quarter', HasQuarterState()),
        (NoQuarterState(), 2, 'turn_crunk', NoQuarterState()),
        (NoQuarterState(), 2, 'eject_quarter', NoQuarterState()),
        (NoQuarterState(), 2, 'dispense', NoQuarterState()),
        (HasQuarterState(), 2, 'insert_quarter', HasQuarterState()),
        (HasQuarterState(), 2, 'turn_crunk', SoldState()),
        (HasQuarterState(), 2, 'eject_quarter', NoQuarterState()),
        (HasQuarterState(), 2, 'dispense', HasQuarterState()),
        (SoldState(), 2, 'insert_quarter', SoldState()),
        (SoldState(), 2, 'turn_crunk', SoldState()),
        (SoldState(), 2, 'eject_quarter', SoldState()),
        (SoldState(), 2, 'dispense', NoQuarterState()),
        (SoldState(), 1, 'dispense', SoldOutState()),
        (SoldOutState(), 0, 'insert_quarter', SoldOutState()),
        (SoldOutState(), 0, 'turn_crunk', SoldOutState()),
        (SoldOutState(), 0, 'eject_quarter', SoldOutState()),
        (SoldOutState(), 0, 'dispense', SoldOutState()),
    ],
)


def test_state_pattern(
    initial_state: State,
    gumballs_amount: int,
    action: str,
    new_state: State,
) -> None:
    """Test state pattern.

    Machine's states should change according to the actions.
    """
    machine = GumballMachine(gumballs_amount, initial_state)

    getattr(machine, action)()

    assert machine.state == new_state
