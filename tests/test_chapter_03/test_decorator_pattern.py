"""Module for testing pattern "Decorator"."""


import pytest

from patterns.chapter_03_decorator.beverages import (
    Beverage,
    DarkRoast,
    Espresso,
    HouseBlend,
)
from patterns.chapter_03_decorator.condiments import (
    Chocolate,
    CondimentDecorator,
    Mocha,
    Soy,
)

pytestmark = pytest.mark.parametrize(
    ('beverage', 'condiments'),
    [
        (DarkRoast(), [Mocha]),
        (HouseBlend(), [Soy]),
        (Espresso(), [Chocolate]),
        (HouseBlend(), [Soy, Chocolate, Mocha]),
    ],
)


def add_condiments_to_beverage(
    beverage: Beverage,
    condiments: list[type[CondimentDecorator]],
) -> Beverage:
    """Add condiments to beverage."""
    for condiment in condiments:
        beverage = condiment(beverage)

    return beverage


def test_total_cost_is_correct(
    beverage: Beverage,
    condiments: list[type[CondimentDecorator]],
) -> None:
    """Test if total calculated cost of beverage with condiments is correct."""
    beverage_with_condiments = add_condiments_to_beverage(beverage, condiments)

    condiments_cost = sum(cond.get_condiment_cost() for cond in condiments)

    assert (condiments_cost + beverage.cost) == beverage_with_condiments.cost


def test_full_description_is_correct(
    beverage: Beverage,
    condiments: list[type[CondimentDecorator]],
) -> None:
    """Test if full description of beverage with condiments is correct."""
    beverage_with_condiments = add_condiments_to_beverage(beverage, condiments)

    for condiment in condiments:
        assert (
            condiment.get_condiment_description()
            in beverage_with_condiments.description
        )
