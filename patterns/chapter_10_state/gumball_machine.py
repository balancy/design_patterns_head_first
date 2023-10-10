"""Gumball machine module."""

from .state import NoQuarterState, SoldOutState, State


class GumballMachine:
    """Gumball machine class."""

    def __init__(
        self,
        gumballs_amount: int,
        initial_state: State | None = None,
    ) -> None:
        """Initialize with state and gubmalls amount."""
        self._state = initial_state or (
            SoldOutState() if gumballs_amount == 0 else NoQuarterState()
        )

        self._gubmalls_amount = gumballs_amount

    @property
    def state(self) -> State:
        """Get current state."""
        return self._state

    def _transition_to(self, new_state: State) -> None:
        """Transition to a new state."""
        if new_state is not self._state:
            self._state = new_state

    def _reduce_gumballs_amount(self, new_state: State) -> None:
        """Reduce gumballs amount."""
        if new_state is not self._state:
            self._gubmalls_amount -= 1

    def insert_quarter(self) -> None:
        """Insert quarter method."""
        new_state: State = self._state.insert_quarter()
        self._transition_to(new_state)

    def eject_quarter(self) -> None:
        """Eject quarter method."""
        new_state: State = self._state.eject_quarter()
        self._transition_to(new_state)

    def turn_crunk(self) -> None:
        """Turn crank method."""
        new_state: State = self._state.turn_crank()
        self._transition_to(new_state)

    def dispense(self) -> None:
        """Dispense gumball method."""
        is_gumball_last = self._gubmalls_amount == 1
        new_state: State = self._state.dispense(is_gumball_last)
        self._reduce_gumballs_amount(new_state)
        self._transition_to(new_state)
