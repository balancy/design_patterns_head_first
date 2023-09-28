from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self) -> None:
        self._description: str = 'Unknown Beverage'

    def get_description(self) -> str:
        return self._description

    @abstractmethod
    def cost(self) -> float:
        ...


class Espresso(Beverage):
    def __init__(self) -> None:
        self._description: str = 'Espresso'
        self._cost: float = 1.99

    @property
    def cost(self) -> float:
        return self._cost


class HouseBlend(Beverage):
    def __init__(self) -> None:
        self._description: str = 'House Blend Coffee'
        self._cost: float = 0.89

    @property
    def cost(self) -> float:
        return self._cost


class DarkRoast(Beverage):
    def __init__(self) -> None:
        self._description: str = 'Dark Roast Coffee'
        self._cost: float = 0.99

    @property
    def cost(self) -> float:
        return self._cost


class Decaffeinated(Beverage):
    def __init__(self) -> None:
        self._description: str = 'Decaffeinated Coffee'
        self._cost: float = 1.05

    def cost(self) -> float:
        return self._cost
