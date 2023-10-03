"""Main entrypoint for the Factory method pattern example."""


from .pizza_stores import ChicagoPizzaStore, NYPizzaStore


def run_pattern_example() -> None:
    """Test factory method example.

    When pizza is ordered, factory creates it and make it ready.
    """
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza = nyStore.order_pizza('cheese')
    print(f'Ethan ordered a {pizza.name}\n')

    pizza = chicagoStore.order_pizza('cheese')
    print(f'Joel ordered a {pizza.name}\n')


if __name__ == '__main__':
    run_pattern_example()
