from abc import ABC, abstractmethod

from .ingredients_factories import NYPizzaIngredientFactory
from .pizzas import CheesePizza, ClamPizza, Pizza


class PizzaStore(ABC):
    @abstractmethod
    def _create_pizza(self, item: str) -> Pizza:
        ...

    def order_pizza(self, item: str) -> Pizza:
        pizza = self._create_pizza(item)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class NYPizzaStore(PizzaStore):
    def _create_pizza(self, item: str) -> Pizza | None:
        pizza: Pizza | None = None
        ingredient_factory = NYPizzaIngredientFactory()

        match item:
            case 'cheese':
                pizza = CheesePizza(ingredient_factory)
                pizza.name = 'New York Style Cheese Pizza'
            case 'clam':
                pizza = ClamPizza(ingredient_factory)
            # and so on

        return pizza
