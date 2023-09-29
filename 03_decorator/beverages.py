from abc import ABC


class Beverage(ABC):
    _description: str
    _cost: float

    def get_description(self) -> str:
        return self._description

    @property
    def cost(self) -> float:
        return self._cost


class Espresso(Beverage):
    _description: str = 'Espresso'
    _cost: float = 1.99


class HouseBlend(Beverage):
    _description: str = 'House Blend Coffee'
    _cost: float = 0.89


class DarkRoast(Beverage):
    _description: str = 'Dark Roast Coffee'
    _cost: float = 0.99


class Decaffeinated(Beverage):
    _description: str = 'Decaffeinated Coffee'
    _cost: float = 1.05
