"""Abstract state class and 4 its implementations."""

from __future__ import annotations

from abc import ABC, abstractmethod


class State(ABC):
    """Abstract state class."""

    @abstractmethod
    def insert_quarter(self) -> State:
        """Abstract insert quarter method.

        All child classes should implement this method.
        """

    @abstractmethod
    def eject_quarter(self) -> State:
        """Abstract eject quarter method.

        All child classes should implement this method.
        """

    @abstractmethod
    def turn_crank(self) -> State:
        """Abstract turn crank method.

        All child classes should implement this method.
        """

    @abstractmethod
    def dispense(self, is_gumball_last: bool) -> State:
        """Abstract dispense gumballn method.

        All child classes should implement this method.
        """

    def __new__(cls) -> State:
        """Return singleton instance.

        If instance is not created, create it and return it.
        If instance is already created, return it.
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(State, cls).__new__(cls)
        return cls.instance


class NoQuarterState(State):
    """No quarter state class."""

    def insert_quarter(self) -> State:
        """Insert quarter method implementation."""
        print("You inserted a quarter")
        return HasQuarterState()

    def eject_quarter(self) -> State:
        """Eject quarter method implementation."""
        print("You haven't inserted a quarter")
        return self.__class__()

    def turn_crank(self) -> State:
        """Turn crank method implementation."""
        print("You turned, but there's no quarter")
        return self.__class__()

    def dispense(self, is_gumball_last: bool) -> State:
        """Dispense gumball method implementation."""
        print("You need to pay first")
        return self.__class__()


class HasQuarterState(State):
    """Has quarter state class."""

    def insert_quarter(self) -> State:
        """Insert quarter method implementation."""
        print("You can't insert another quarter")
        return self.__class__()

    def eject_quarter(self) -> State:
        """Eject quarter method implementation."""
        print("Quarter returned")
        return NoQuarterState()

    def turn_crank(self) -> State:
        """Turn crank method implementation."""
        print("You turned...")
        return SoldState()

    def dispense(self, is_gumball_last: bool) -> State:
        """Dispense gumball method implementation."""
        print("No gumball dispensed")
        return self.__class__()


class SoldState(State):
    """Sold state class."""

    def insert_quarter(self) -> State:
        """Insert quarter method implementation."""
        print("Wait for ball")
        return self.__class__()

    def eject_quarter(self) -> State:
        """Eject quarter method implementation."""
        print("You already turned crank")
        return self.__class__()

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

    def insert_quarter(self) -> State:
        """Insert quarter method implementation."""
        print("You can't insert a quarter, the machine is sold out")
        return self.__class__()

    def eject_quarter(self) -> State:
        """Eject quarter method implementation."""
        print("You haven't inserted a quarter")
        return self.__class__()

    def turn_crank(self) -> State:
        """Turn crank method implementation."""
        print("You turned, but there is no gumballs")
        return self.__class__()

    def dispense(self, is_gumball_last: bool) -> State:
        """Dispense gumball method implementation."""
        print("No gumball dispensed")
        return self.__class__()
