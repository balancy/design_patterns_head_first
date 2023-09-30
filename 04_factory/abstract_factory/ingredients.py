from abc import ABC, abstractmethod


class Dough(ABC):
    @abstractmethod
    def __repr__(self) -> str:
        ...


class ThinCrustDough(Dough):
    def __repr__(self) -> str:
        return 'Thin Crust Dough'


class ThickCrustDough(Dough):
    def __repr__(self) -> str:
        return 'Thick Crust Dough'


class Sauce(ABC):
    @abstractmethod
    def __repr__(self) -> str:
        ...


class MarinaraSauce(Sauce):
    def __repr__(self) -> str:
        return 'Marinara Sauce'


class PlumTomatoSauce(Sauce):
    def __repr__(self) -> str:
        return 'Plum Tomato Sauce'


class Cheese(ABC):
    @abstractmethod
    def __repr__(self) -> str:
        ...


class MozarellaCheese(Cheese):
    def __repr__(self) -> str:
        return 'Mozarella Cheese'


class ReggianoCheese(Cheese):
    def __repr__(self) -> str:
        return 'Reggiano Cheese'


class Pepperoni(ABC):
    @abstractmethod
    def __repr__(self) -> str:
        ...


class SlicedPepperoni(Pepperoni):
    def __repr__(self) -> str:
        return 'Sliced Pepperoni'


class Clams(ABC):
    @abstractmethod
    def __repr__(self) -> str:
        ...


class FrozenClams(Clams):
    def __repr__(self) -> str:
        return 'Frozen Clams'


class FreshClams(Clams):
    def __repr__(self) -> str:
        return 'Fresh Clams'


class Veggie(ABC):
    @abstractmethod
    def __repr__(self) -> str:
        ...


class Veggies(ABC):
    def __init__(self, *ingredients) -> None:
        self._ingredients = ingredients

    def __repr__(self) -> str:
        return ', '.join(self._ingredients)


class Garlic(Veggie):
    def __repr__(self) -> str:
        return 'Garlic'


class Onion(Veggie):
    def __repr__(self) -> str:
        return 'Onion'


class Mushroom(Veggie):
    def __repr__(self) -> str:
        return 'Mushroom'


class RedPepper(Veggie):
    def __repr__(self) -> str:
        return 'Red Pepper'
