"""Module for testing pattern "Factory method"."""

import pytest

from patterns.chapter_04_factory_method.pizza_stores import (
    ChicagoPizzaStore,
    NYPizzaStore,
    PizzaStore,
)

pytestmark = pytest.mark.parametrize(
    ('store'),
    [NYPizzaStore(), ChicagoPizzaStore()],
)


def test_factory_method(capsys, store: PizzaStore) -> None:
    """Test fdactory method patterns.

    Pizza name should appear in output when we order pizza via factory method.
    """
    pizza = store.order_pizza('cheese')
    captured = capsys.readouterr()

    assert pizza.name in captured.out
