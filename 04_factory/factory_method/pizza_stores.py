from abc import ABC, abstractmethod

from .pizzas import ChicagoStyleCheesePizza, NYStyleCheesePizza, Pizza


class PizzaStore(ABC):
    @abstractmethod
    def _create_pizza(self, pizza_type: str) -> Pizza:
        ...

    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza = self._create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class NYPizzaStore(PizzaStore):
    def _create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == 'cheese':
            return NYStyleCheesePizza()
        # and so on
        else:
            raise ValueError(f'Unknown pizza type {pizza_type}')


class ChicagoPizzaStore(PizzaStore):
    def _create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == 'cheese':
            return ChicagoStyleCheesePizza()
        # and so on
        else:
            raise ValueError(f'Unknown pizza type {pizza_type}')
