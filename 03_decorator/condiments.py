from abc import abstractmethod

from .beverages import Beverage


class CondimentDecorator(Beverage):
    @abstractmethod
    def get_description(self) -> str:
        ...


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage

    def get_description(self) -> str:
        return self._beverage.get_description() + ', Mocha'

    def cost(self) -> float:
        return 0.10 + self._beverage.cost()


class Chocolate(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage

    def get_description(self) -> str:
        return self._beverage.get_description() + ', Chocolate'

    def cost(self) -> float:
        return 0.20 + self._beverage.cost()


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage

    def get_description(self) -> str:
        return self._beverage.get_description() + ', Soy'

    def cost(self) -> float:
        return 0.15 + self._beverage.cost()
