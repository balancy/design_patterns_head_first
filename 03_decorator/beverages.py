from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self) -> None:
        self._description = 'Unknown Beverage'

    def get_description(self) -> str:
        return self._description

    @abstractmethod
    def cost(self) -> float:
        ...


class Espresso(Beverage):
    def __init__(self) -> None:
        self._description = 'Espresso'

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    def __init__(self) -> None:
        self._description = 'House Blend Coffee'

    def cost(self) -> float:
        return 0.89


class DarkRoast(Beverage):
    def __init__(self) -> None:
        self._description = 'Dark Roast Coffee'

    def cost(self) -> float:
        return 0.99


class Decaffeinated(Beverage):
    def __init__(self) -> None:
        self._description = 'Decaffeinated Coffee'

    def cost(self) -> float:
        return 1.05
