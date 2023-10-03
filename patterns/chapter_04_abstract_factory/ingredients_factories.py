"""Pizza ingredients factories: basic abstract and one child implementation."""

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
    """Abstract pizza ingredients factory class."""

    @abstractmethod
    def create_dough(self) -> Dough:
        """Abstract create dough method.

        All child classes must implement this method.
        """
        ...

    @abstractmethod
    def create_sauce(self) -> Sauce:
        """Abstract create sauce method.

        All child classes must implement this method.
        """
        ...

    @abstractmethod
    def create_cheese(self) -> Cheese:
        """Abstract create cheese method.

        All child classes must implement this method.
        """
        ...

    @abstractmethod
    def create_veggies(self) -> Veggies:
        """Abstract create veggies method.

        All child classes must implement this method.
        """
        ...

    @abstractmethod
    def create_pepperoni(self) -> Pepperoni:
        """Abstract create pepperoni method.

        All child classes must implement this method.
        """
        ...

    @abstractmethod
    def create_clam(self) -> Clams:
        """Abstract create clams method.

        All child classes must implement this method.
        """
        ...


class NYPizzaIngredientFactory(PizzaIngdredientFactory):
    """New York pizza ingredients factory class."""

    def create_dough(self) -> Dough:
        """One of implementations of abstract parent method."""
        return ThinCrustDough()

    def create_sauce(self) -> Sauce:
        """One of implementations of abstract parent method."""
        return MarinaraSauce()

    def create_cheese(self) -> Cheese:
        """One of implementations of abstract parent method."""
        return ReggianoCheese()

    def create_veggies(self) -> Veggies:
        """One of implementations of abstract parent method."""
        veggies: Veggies = Veggies(
            ingredients=[Garlic(), Onion(), Mushroom(), RedPepper()]
        )
        return veggies

    def create_pepperoni(self) -> Pepperoni:
        """One of implementations of abstract parent method."""
        return SlicedPepperoni()

    def create_clam(self) -> Clams:
        """One of implementations of abstract parent method."""
        return FreshClams()
