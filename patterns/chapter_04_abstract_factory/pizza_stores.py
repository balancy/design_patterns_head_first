"""Base abstract pizza store class (factory class) and two child classes."""

from abc import ABC, abstractmethod

from .ingredients_factories import NYPizzaIngredientFactory
from .pizzas import CheesePizza, ClamPizza, Pizza


class PizzaStore(ABC):
    """Base abstract pizza factory class."""

    @abstractmethod
    def _create_pizza(self, item: str) -> Pizza:
        """Abstract factory method for creating pizza.

        All child classes must implement this method.
        """
        ...

    def order_pizza(self, item: str) -> Pizza:
        """Order pizza.

        While ordering, factory will create new pizza and make it ready.
        """
        pizza = self._create_pizza(item)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class NYPizzaStore(PizzaStore):
    """New York pizza factory class."""

    def _create_pizza(self, item: str) -> Pizza:
        pizza: Pizza
        ingredient_factory = NYPizzaIngredientFactory()
        prefix = 'New York Style'

        match item:
            case 'cheese':
                pizza = CheesePizza(ingredient_factory)
                pizza.name = f'{prefix} Cheese Pizza'
            case 'clam':
                pizza = ClamPizza(ingredient_factory)
                pizza.name = f'{prefix} Clam Pizza'
            # and so on
            case _:
                raise ValueError(f'Unknown pizza type {item}')

        return pizza
