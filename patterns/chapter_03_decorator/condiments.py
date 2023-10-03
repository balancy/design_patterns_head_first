"""Basic condiment class and 3 child classes."""


from decimal import Decimal

from .beverages import Beverage


class CondimentDecorator(Beverage):
    """Basic condiment decorator class."""

    def __init__(self, beverage: Beverage) -> None:
        """Initialize condiment decorator instance."""
        self._beverage = beverage

    @property
    def description(self) -> str:
        """Get beverage with condiment description."""
        return f'{self._beverage.description}, {self.__class__.__name__}'

    @property
    def cost(self) -> Decimal:
        """Get beverage with condiment cost."""
        return self._cost + self._beverage.cost

    @classmethod
    def get_condiment_cost(cls) -> Decimal:
        """Get condiment cost."""
        return cls._cost

    @classmethod
    def get_condiment_description(cls) -> str:
        """Get condiment description."""
        return cls.__name__


class Mocha(CondimentDecorator):
    """Mocha condiment decorator."""

    _cost = Decimal('0.10')


class Chocolate(CondimentDecorator):
    """Chocolate condiment decorator."""

    _cost = Decimal('0.20')


class Soy(CondimentDecorator):
    """Soy condiment decorator."""

    _cost = Decimal('0.15')
