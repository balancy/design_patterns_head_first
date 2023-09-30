from abc import ABC, abstractmethod

from .ingredients_factories import PizzaIngdredientFactory


class Pizza(ABC):
    def __init__(self, ingredient_factory: PizzaIngdredientFactory) -> None:
        self._ingredient_factory = ingredient_factory
        self._name = self.__class__.__name__

    @abstractmethod
    def prepare(self) -> None:
        ...

    def bake(self) -> None:
        print('Bake for 25 minutes at 350')

    def cut(self) -> None:
        print('Cutting the pizza into diagonal slices')

    def box(self) -> None:
        print('Place pizza in official PizzaStore box')

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    def __repr__(self) -> str:
        return self.__name__


class CheesePizza(Pizza):
    def prepare(self) -> None:
        print(f'Preparing {self.name}')
        dough = str(self._ingredient_factory.create_dough())
        sauce = str(self._ingredient_factory.create_sauce())
        cheese = str(self._ingredient_factory.create_cheese())
        print('With ingredients:', ', '.join([dough, sauce, cheese]))


class ClamPizza(Pizza):
    def prepare(self) -> None:
        print(f'Preparing {self.name}')
        dough = str(self._ingredient_factory.create_dough())
        sauce = str(self._ingredient_factory.create_sauce())
        cheese = str(self._ingredient_factory.create_cheese())
        clam = str(self._ingredient_factory.create_clam())
        print('With ingredients:', ', '.join([dough, sauce, cheese, clam]))
