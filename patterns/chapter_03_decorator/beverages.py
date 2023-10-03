"""Basic beverage class and 4 child classes."""

from decimal import Decimal


class Beverage:
    """Basic class for beverage."""

    _description: str
    _cost: Decimal

    @property
    def description(self) -> str:
        """Get beverage description."""
        return self._description

    @property
    def cost(self) -> Decimal:
        """Get beverage cost."""
        return self._cost


class Espresso(Beverage):
    """Espresso beverage."""

    _description = 'Espresso'
    _cost = Decimal('1.99')


class HouseBlend(Beverage):
    """House Blend beverage."""

    _description = 'House Blend Coffee'
    _cost = Decimal('0.89')


class DarkRoast(Beverage):
    """Dark Roast beverage."""

    _description = 'Dark Roast Coffee'
    _cost = Decimal('0.99')


class Decaffeinated(Beverage):
    """Decaffeinated beverage."""

    _description = 'Decaffeinated Coffee'
    _cost = Decimal('1.05')
