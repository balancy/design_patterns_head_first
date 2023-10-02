"""Main entrypoint for the Decorator pattern example."""


from .beverages import Beverage, DarkRoast, Espresso
from .condiments import Chocolate, Mocha, Soy


def run_pattern_example() -> None:
    """Test decorator example.

    Additional condiments change price and description of the beverage.
    """
    espresso: Beverage = Espresso()
    print(f'{espresso.description} ${espresso.cost}')

    dark_roast: Beverage = DarkRoast()
    for condiment in [Mocha, Soy, Chocolate]:
        dark_roast = condiment(dark_roast)

    print(f'{dark_roast.description} ${dark_roast.cost}')


if __name__ == '__main__':
    run_pattern_example()
