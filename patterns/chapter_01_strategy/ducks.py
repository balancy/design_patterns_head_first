"""Abstract class for duck and three concrete implementations."""

from abc import ABC, abstractmethod

from .fly_behaviour import FlyBehavior, FlyNoWay, FlyWithWings
from .quack_behaviour import MuteQuack, Quack, QuackBehavior, Squeak


class Duck(ABC):
    """Abstract class for ducks."""

    @abstractmethod
    def display(self) -> None:
        """Abstract method for displaying duck.

        All child classes should implement this method.
        """
        ...

    def swim(self) -> None:
        """Perform swim behavior."""
        print('All ducks float, even decoys!')

    def perform_fly(self) -> None:
        """Perform fly behavior."""
        self._fly_behaviour.perform_fly()

    def set_fly_behavior(self, fly_behaviour: FlyBehavior) -> None:
        """Set fly behavior."""
        self._fly_behaviour = fly_behaviour

    def perform_quack(self) -> None:
        """Perform quack behavior."""
        self._quack_behaviour.perform_quack()

    def set_quack_behavior(self, quack_behaviour: QuackBehavior) -> None:
        """Set quack behavior."""
        self._quack_behaviour = quack_behaviour


class MaillardDuck(Duck):
    """Concrete class for Maillard duck."""

    def __init__(self) -> None:
        """Initialize Maillard duck."""
        self._fly_behaviour: FlyBehavior = FlyWithWings()
        self._quack_behaviour: QuackBehavior = Quack()

    def display(self) -> None:
        """Display Maillard duck."""
        print('I\'m a real Maillard duck')


class RubberDuck(Duck):
    """Concrete class for rubber duck."""

    def __init__(self) -> None:
        """Initialize rubber duck."""
        self._fly_behaviour: FlyBehavior = FlyNoWay()
        self._quack_behaviour: QuackBehavior = Squeak()

    def display(self) -> None:
        """Display rubber duck."""
        print('I\'m a rubber duck')


class DecoyDuck(Duck):
    """Concrete class for decoy duck."""

    def __init__(self) -> None:
        """Initialize decoy duck."""
        self._fly_behaviour: FlyBehavior = FlyNoWay()
        self._quack_behaviour: QuackBehavior = MuteQuack()

    def display(self) -> None:
        """Display decoy duck."""
        print('I\'m a duck decoy')
