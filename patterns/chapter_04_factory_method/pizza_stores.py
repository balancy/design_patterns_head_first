"""Base abstract pizza store class (factory class) and two child classes."""

from abc import ABC, abstractmethod

from .pizzas import ChicagoStyleCheesePizza, NYStyleCheesePizza, Pizza


class PizzaStore(ABC):
    """Base pizza factory class."""

    @abstractmethod
    def _create_pizza(self, pizza_type: str) -> Pizza:
        """Abstract factory method for creating pizza.

        All child classes must implement this method.
        """
        ...

    def order_pizza(self, pizza_type: str) -> Pizza:
        """Order pizza.

        While ordering, factory will create new pizza and make it ready.
        """
        pizza = self._create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class NYPizzaStore(PizzaStore):
    """New York pizza factory class."""

    def _create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == 'cheese':
            return NYStyleCheesePizza()
        # and so on
        else:
            raise ValueError(f'Unknown pizza type {pizza_type}')


class ChicagoPizzaStore(PizzaStore):
    """Chicago pizza factory class."""

    def _create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == 'cheese':
            return ChicagoStyleCheesePizza()
        # and so on
        else:
            raise ValueError(f'Unknown pizza type {pizza_type}')
