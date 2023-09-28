from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def perform_fly(self) -> None:
        pass


class FlyWithWings(FlyBehavior):
    def perform_fly(self) -> None:
        print('I\'m flying!')


class FlyNoWay(FlyBehavior):
    def perform_fly(self) -> None:
        print('I can\'t fly')
