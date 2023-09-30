from .pizza_stores import NYPizzaStore


def run() -> None:
    nyStore = NYPizzaStore()

    pizza = nyStore.order_pizza('clam')
    print(f'Ethan ordered a {pizza.name}\n')
