from .pizza_stores import ChicagoPizzaStore, NYPizzaStore


def run() -> None:
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza = nyStore.order_pizza('cheese')
    print(f'Ethan ordered a {pizza.name}\n')

    pizza = chicagoStore.order_pizza('cheese')
    print(f'Joel ordered a {pizza.name}\n')
