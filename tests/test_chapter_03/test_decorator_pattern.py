"""Module for testing pattern "Decorator"."""

from copy import copy

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


@pytest.mark.parametrize(
    ('beverage', 'condiments'),
    [
        (DarkRoast(), [Mocha]),
        (HouseBlend(), [Soy]),
        (Espresso(), [Chocolate]),
        (HouseBlend(), [Soy, Chocolate, Mocha]),
    ],
)
def test_total_cost(
    beverage: Beverage,
    condiments: list[type[CondimentDecorator]],
) -> None:
    """Test pattern as black box."""
    beverage_with_condiments = copy(beverage)
    for condiment in condiments:
        beverage_with_condiments = condiment(beverage_with_condiments)

    condiments_cost = round(
        sum(cond.get_condiment_cost() for cond in condiments), 2
    )
    assert (condiments_cost + beverage.cost) == beverage_with_condiments.cost
