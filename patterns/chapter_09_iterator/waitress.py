"""Waitress class for printing menus."""

from typing import Iterable, cast

from .iterators import MenuIterator
from .menus import Menu


class Waitress:
    """Waitress class."""

    def __init__(self, menus: Iterable[Menu]) -> None:
        """Initialize waitress with menus."""
        self._menus = menus

    def print_all_menus(self) -> None:
        """Print all menus."""
        for menu in self._menus:
            print(menu)
            iterator = menu.create_iterator()
            self._print_menu(iterator)

    def _print_menu(self, iterator: MenuIterator) -> None:
        """Print one menu."""
        for item, price, *_ in iterator:
            print(f'- {cast(str, item)}: {price}')
