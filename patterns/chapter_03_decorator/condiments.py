"""Basic condiment class and 3 child classes."""


from .beverages import Beverage


class CondimentDecorator(Beverage):
    """Basic condiment decorator class."""

    _cost: float

    def __init__(self, beverage: Beverage) -> None:
        """Initialize condiment decorator instance."""
        self._beverage = beverage

    @property
    def description(self) -> str:
        """Get beverage with condiment description."""
        return f'{self._beverage.description}, {self.__class__.__name__}'

    @property
    def cost(self) -> float:
        """Get beverage with condiment cost."""
        return self._cost + self._beverage.cost

    @classmethod
    def get_condiment_cost(cls) -> float:
        """Get condiment cost."""
        return cls._cost


class Mocha(CondimentDecorator):
    """Mocha condiment decorator."""

    _cost = 0.10


class Chocolate(CondimentDecorator):
    """Chocolate condiment decorator."""

    _cost = 0.20


class Soy(CondimentDecorator):
    """Soy condiment decorator."""

    _cost = 0.15
