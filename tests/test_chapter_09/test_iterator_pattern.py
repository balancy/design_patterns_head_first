"""Module for testing pattern "Iterator"."""


import pytest

from patterns.chapter_09_iterator.menus import DinerMenu, Menu, PancackeMenu
from patterns.chapter_09_iterator.waitress import Waitress

pytestmark = pytest.mark.parametrize(
    ('menu', 'menu_items'),
    [
        (PancackeMenu(), {'pancake': 1.99, 'waffle': 2.99}),
        (DinerMenu(), [('spaghetti', 3.99)]),
    ],
)


def test_iterator_pattern(
    capsys,
    menu: Menu,
    menu_items: list[tuple[str, float]] | dict[str, float],
) -> None:
    """Test iterator pattern.

    Printing all menus must be unified even if menu_items are of different
    types.
    """
    menu.set_items(menu_items)

    Waitress([menu]).print_all_menus()
    captured = capsys.readouterr()

    assert str(menu) in captured.out
