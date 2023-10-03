"""Module for testing pattern "Template method"."""


import pytest

from patterns.chapter_08_template_method.beverages import (
    CaffeineBeverage,
    Coffee,
    Tea,
)

pytestmark = pytest.mark.parametrize(('beverage'), [Tea(), Coffee()])


def test_template_method_pattern(capsys, beverage: CaffeineBeverage) -> None:
    """Test template method pattern.

    Calling prepare_recipe method of child class should call all incapsulated
    methods of parent class.
    """
    beverage.prepare_recipe()

    captured = capsys.readouterr()

    assert str(beverage).lower() in captured.out
