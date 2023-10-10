"""Abstract state class and 4 its implementations."""

from __future__ import annotations

from abc import ABC, abstractmethod


class State(ABC):
    """Abstract state class."""

    @abstractmethod
    def insert_quarter(self) -> State | None:
        """Abstract insert quarter method.

        All child classes should implement this method.
        """

    @abstractmethod
    def eject_quarter(self) -> State | None:
        """Abstract eject quarter method.

        All child classes should implement this method.
        """

    @abstractmethod
    def turn_crank(self) -> State | None:
        """Abstract turn crank method.

        All child classes should implement this method.
        """

    @abstractmethod
    def dispense(self, is_gumball_last: bool) -> State | None:
        """Abstract dispense gumballn method.

        All child classes should implement this method.
        """


class NoQuarterState(State):
    """No quarter state class."""

    def insert_quarter(self) -> State:
        """Insert quarter method implementation."""
        print("You inserted a quarter")
        return HasQuarterState()

    def eject_quarter(self) -> None:
        """Eject quarter method implementation."""
        print("You haven't inserted a quarter")

    def turn_crank(self) -> None:
        """Turn crank method implementation."""
        print("You turned, but there's no quarter")

    def dispense(self, is_gumball_last: bool) -> None:
        """Dispense gumball method implementation."""
        print("You need to pay first")


class HasQuarterState(State):
    """Has quarter state class."""

    def insert_quarter(self) -> None:
        """Insert quarter method implementation."""
        print("You can't insert another quarter")

    def eject_quarter(self) -> State:
        """Eject quarter method implementation."""
        print("Quarter returned")
        return NoQuarterState()

    def turn_crank(self) -> State:
        """Turn crank method implementation."""
        print("You turned...")
        return SoldState()

    def dispense(self, is_gumball_last: bool) -> None:
        """Dispense gumball method implementation."""
        print("No gumball dispensed")


class SoldState(State):
    """Sold state class."""

    def insert_quarter(self) -> None:
        """Insert quarter method implementation."""
        print("Wait for ball")

    def eject_quarter(self) -> None:
        """Eject quarter method implementation."""
        print("You already turned crank")

    def turn_crank(self) -> State:
        """Turn crank method implementation."""
        print("Even if you turn twice you got one ball")
        return SoldState()

    def dispense(self, is_gumball_last: bool) -> State:
        """Dispense gumball method implementation."""
        print("A gumball comes rolling out the slot...")
        if not is_gumball_last:
            return NoQuarterState()

        print('Machine is sold out!')
        return SoldOutState()


class SoldOutState(State):
    """Sold out state class."""

    def insert_quarter(self) -> None:
        """Insert quarter method implementation."""
        print("You can't insert a quarter, the machine is sold out")

    def eject_quarter(self) -> None:
        """Eject quarter method implementation."""
        print("You haven't inserted a quarter")

    def turn_crank(self) -> None:
        """Turn crank method implementation."""
        print("You turned, but there is no gumballs")

    def dispense(self, is_gumball_last: bool) -> None:
        """Dispense gumball method implementation."""
        print("No gumball dispensed")
