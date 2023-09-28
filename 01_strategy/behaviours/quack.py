from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    @abstractmethod
    def perform_quack(self) -> None:
        pass


class Quack(QuackBehavior):
    def perform_quack(self) -> None:
        print('Quack')


class MuteQuack(QuackBehavior):
    def perform_quack(self) -> None:
        print('<< Silence >>')


class Squeak(QuackBehavior):
    def perform_quack(self) -> None:
        print('Squeak')
