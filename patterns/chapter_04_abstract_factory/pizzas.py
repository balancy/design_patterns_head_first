"""Base abstract pizza class and two child classes."""

from abc import ABC, abstractmethod

from .ingredients_factories import PizzaIngdredientFactory


class Pizza(ABC):
    """Base abstract pizza class."""

    def __init__(self, ingredient_factory: PizzaIngdredientFactory) -> None:
        """Initialize 'pizza with ingredients' factory."""
        self._ingredient_factory = ingredient_factory
        self._name = self.__class__.__name__

    @abstractmethod
    def prepare(self) -> None:
        """Abstract method for preparing pizza.

        All child classes must implement this method.
        """
        ...

    def bake(self) -> None:
        """Bake pizza."""
        print('Bake for 25 minutes at 350')

    def cut(self) -> None:
        """Cut pizza."""
        print('Cutting the pizza into diagonal slices')

    def box(self) -> None:
        """Box pizza."""
        print('Place pizza in official PizzaStore box')

    @property
    def name(self) -> str:
        """Return pizza name."""
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """Set pizza name."""
        self._name = name

    def __repr__(self) -> str:
        """Return pizza representation."""
        return self._name


class CheesePizza(Pizza):
    """Cheese pizza class."""

    def prepare(self) -> None:
        """Prepare pizza."""
        print(f'Preparing {self.name}')
        dough = str(self._ingredient_factory.create_dough())
        sauce = str(self._ingredient_factory.create_sauce())
        cheese = str(self._ingredient_factory.create_cheese())
        print('With ingredients:', ', '.join([dough, sauce, cheese]))


class ClamPizza(Pizza):
    """Clam pizza class."""

    def prepare(self) -> None:
        """Prepare pizza."""
        print(f'Preparing {self.name}')
        dough = str(self._ingredient_factory.create_dough())
        sauce = str(self._ingredient_factory.create_sauce())
        cheese = str(self._ingredient_factory.create_cheese())
        clam = str(self._ingredient_factory.create_clam())
        print('With ingredients:', ', '.join([dough, sauce, cheese, clam]))
