class Pizza:
    _name: str
    _dough: str
    _sauce: str
    _toppings: list[str]

    def prepare(self) -> None:
        print(f'Preparing {self._name}')
        print('Tossing dough...')
        print('Adding sauce...')
        print('Adding toppings:')
        for topping in self._toppings:
            print(f'    {topping}')

    def bake(self) -> None:
        print('Bake for 25 minutes at 350')

    def cut(self) -> None:
        print('Cutting the pizza into diagonal slices')

    def box(self) -> None:
        print('Place pizza in official PizzaStore box')

    @property
    def name(self) -> str:
        return self._name


class NYStyleCheesePizza(Pizza):
    _name = 'NY Style Sauce and Cheese Pizza'
    _dough = 'Thin Crust Dough'
    _sauce = 'Marinara Sauce'
    _toppings = ['Grated Reggiano Cheese']


class ChicagoStyleCheesePizza(Pizza):
    _name = 'Chicago Style Deep Dish Cheese Pizza'
    _dough = 'Extra Thick Crust Dough'
    _sauce = 'Plum Tomato Sauce'
    _toppings = ['Shredded Mozzarella Cheese']

    def cut(self) -> None:
        print('Cutting the pizza into square slices')
