"""Gumball machine module."""
from .state import NoQuarterState, SoldOutState, State


class GumballMachine:
    """Gumball machine class."""

    def __init__(self, gumballs_amount: int) -> None:
        """Initialize with state and gubmalls amount."""
        self._state: State = (
            NoQuarterState() if gumballs_amount > 0 else SoldOutState()
        )
        self._gubmalls_amount = gumballs_amount

    def _transition_to(self, state: State | None) -> None:
        """Transition to a new state."""
        if state is not None:
            self._state = state

    def insert_quarter(self) -> None:
        """Insert quarter method."""
        new_state: State | None = self._state.insert_quarter()
        self._transition_to(new_state)

    def eject_quarter(self) -> None:
        """Eject quarter method."""
        new_state: State | None = self._state.eject_quarter()
        self._transition_to(new_state)

    def turn_crunk(self) -> None:
        """Turn crank method."""
        new_state: State | None = self._state.turn_crank()
        self._transition_to(new_state)

    def dispense(self) -> None:
        """Dispense gumball method."""
        is_gumball_last = self._gubmalls_amount == 1
        new_state: State | None = self._state.dispense(is_gumball_last)
        if new_state is not None:
            self._gubmalls_amount -= 1
        self._transition_to(new_state)
