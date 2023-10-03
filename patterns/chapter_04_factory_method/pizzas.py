"""Base pizza class and two child pizza classes."""


class Pizza:
    """Base pizza class."""

    _name: str
    _dough: str
    _sauce: str
    _toppings: list[str]

    def prepare(self) -> None:
        """Prepare pizza, including adding all toppings."""
        print(f'Preparing {self._name}')
        print('Tossing dough...')
        print('Adding sauce...')
        print('Adding toppings:')
        for topping in self._toppings:
            print(f'    {topping}')

    def bake(self) -> None:
        """Bake pizza."""
        print('Bake for 25 minutes at 350')

    def cut(self) -> None:
        """Cut pizza into slices."""
        print('Cutting the pizza into diagonal slices')

    def box(self) -> None:
        """Box pizza."""
        print('Place pizza in official PizzaStore box')

    @property
    def name(self) -> str:
        """Return pizza name."""
        return self._name


class NYStyleCheesePizza(Pizza):
    """New York style cheese pizza."""

    _name = 'NY Style Sauce and Cheese Pizza'
    _dough = 'Thin Crust Dough'
    _sauce = 'Marinara Sauce'
    _toppings = ['Grated Reggiano Cheese']


class ChicagoStyleCheesePizza(Pizza):
    """Chicago style cheese pizza."""

    _name = 'Chicago Style Deep Dish Cheese Pizza'
    _dough = 'Extra Thick Crust Dough'
    _sauce = 'Plum Tomato Sauce'
    _toppings = ['Shredded Mozzarella Cheese']

    def cut(self) -> None:
        """Override base cut method for this pizza type implementation."""
        print('Cutting the pizza into square slices')
