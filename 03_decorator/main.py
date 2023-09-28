from .beverages import Beverage, DarkRoast, Espresso
from .condiments import Chocolate, Mocha, Soy


def run() -> None:
    espresson: Beverage = Espresso()
    print(f'{espresson.get_description()} ${espresson.cost}')

    dark_roast: Beverage = DarkRoast()
    for condiment in (Mocha, Soy, Chocolate, Mocha):
        dark_roast = condiment(dark_roast)
    print(f'{dark_roast.get_description()} ${dark_roast.cost}')


if __name__ == '__main__':
    run()
