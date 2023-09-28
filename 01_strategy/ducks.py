from abc import ABC, abstractmethod

from .behaviours.fly import FlyBehavior, FlyNoWay, FlyWithWings
from .behaviours.quack import MuteQuack, Quack, QuackBehavior, Squeak


class Duck(ABC):
    def __init__(self) -> None:
        self._fly_behaviour: FlyBehavior = FlyWithWings()
        self._quack_behaviour: QuackBehavior = Quack()

    @abstractmethod
    def display(self) -> None:
        ...

    def swim(self) -> None:
        print('All ducks float, even decoys!')

    def perform_fly(self) -> None:
        self._fly_behaviour.perform_fly()

    def set_fly_behavior(self, fly_behaviour: FlyBehavior) -> None:
        self._fly_behaviour = fly_behaviour

    def perform_quack(self) -> None:
        self._quack_behaviour.perform_quack()

    def set_quack_behavior(self, quack_behaviour: QuackBehavior) -> None:
        self._quack_behaviour = quack_behaviour


class MaillardDuck(Duck):
    def display(self) -> None:
        print('I\'m a real Maillard duck')


class RubberDuck(Duck):
    def __init__(self) -> None:
        self._fly_behaviour: FlyBehavior = FlyNoWay()
        self._quack_behaviour: QuackBehavior = Squeak()

    def display(self) -> None:
        print('I\'m a rubber duck')


class DecoyDuck(Duck):
    def __init__(self) -> None:
        self._fly_behaviour: FlyBehavior = FlyNoWay()
        self._quack_behaviour: QuackBehavior = MuteQuack()

    def display(self) -> None:
        print('I\'m a duck decoy')
