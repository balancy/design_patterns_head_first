from typing import cast

from .beverages import Beverage


class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage

    def get_description(self) -> str:
        return self._beverage.get_description() + ', ' + self.__class__.__name__


class Mocha(CondimentDecorator):
    _cost = 0.10

    @property
    def cost(self) -> float:
        return self._cost + cast(float, self._beverage.cost)


class Chocolate(CondimentDecorator):
    _cost = 0.20

    @property
    def cost(self) -> float:
        return self._cost + cast(float, self._beverage.cost)


class Soy(CondimentDecorator):
    _cost = 0.15

    @property
    def cost(self) -> float:
        return self._cost + cast(float, self._beverage.cost)
