from abc import ABC, abstractmethod

from .ingredients import (
    Cheese,
    Clams,
    Dough,
    FreshClams,
    Garlic,
    MarinaraSauce,
    Mushroom,
    Onion,
    Pepperoni,
    RedPepper,
    ReggianoCheese,
    Sauce,
    SlicedPepperoni,
    ThinCrustDough,
    Veggies,
)


class PizzaIngdredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough:
        ...

    @abstractmethod
    def create_sauce(self) -> Sauce:
        ...

    @abstractmethod
    def create_cheese(self) -> Cheese:
        ...

    @abstractmethod
    def create_veggies(self) -> Veggies:
        ...

    @abstractmethod
    def create_pepperoni(self) -> Pepperoni:
        ...

    @abstractmethod
    def create_clam(self) -> Clams:
        ...


class NYPizzaIngredientFactory(PizzaIngdredientFactory):
    def create_dough(self) -> Dough:
        return ThinCrustDough()

    def create_sauce(self) -> Sauce:
        return MarinaraSauce()

    def create_cheese(self) -> Cheese:
        return ReggianoCheese()

    def create_veggies(self) -> Veggies:
        veggies: Veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_clam(self) -> Clams:
        return FreshClams()
