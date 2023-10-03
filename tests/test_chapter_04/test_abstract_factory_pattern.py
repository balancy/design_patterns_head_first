"""Module for testing pattern "Factory method"."""

import pytest

from patterns.chapter_04_abstract_factory.pizza_stores import NYPizzaStore

pytestmark = pytest.mark.parametrize('pizza_type', ['cheese', 'clam'])


def test_factory_method(capsys, pizza_type: str) -> None:
    """Test abstract factory patterns.

    Pizza name should appear in output when ordering pizza via abstract
    factory.
    """
    pizza = NYPizzaStore().order_pizza(pizza_type)
    captured = capsys.readouterr()

    assert pizza.name in captured.out
