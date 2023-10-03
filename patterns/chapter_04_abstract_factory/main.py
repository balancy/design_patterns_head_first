"""Main entrypoint for the Abstract factory pattern example."""

from .pizza_stores import NYPizzaStore


def run_pattern_example() -> None:
    """Test abstract factory example.

    When pizza is ordered, factory creates it and make it ready.
    """
    nyStore = NYPizzaStore()

    pizza = nyStore.order_pizza('clam')
    print(f'Ethan ordered a {pizza.name}\n')


if __name__ == '__main__':
    run_pattern_example()
