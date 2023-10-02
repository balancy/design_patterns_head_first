"""Basic beverage class and 4 child classes."""


class Beverage:
    """Basic class for beverage."""

    _description: str
    _cost: float

    @property
    def description(self) -> str:
        """Get beverage description."""
        return self._description

    @property
    def cost(self) -> float:
        """Get beverage cost."""
        return self._cost


class Espresso(Beverage):
    """Espresso beverage."""

    _description: str = 'Espresso'
    _cost: float = 1.99


class HouseBlend(Beverage):
    """House Blend beverage."""

    _description: str = 'House Blend Coffee'
    _cost: float = 0.89


class DarkRoast(Beverage):
    """Dark Roast beverage."""

    _description: str = 'Dark Roast Coffee'
    _cost: float = 0.99


class Decaffeinated(Beverage):
    """Decaffeinated beverage."""

    _description: str = 'Decaffeinated Coffee'
    _cost: float = 1.05
