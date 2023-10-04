"""Iterator module."""

from __future__ import annotations

from .menus import DinerMenu, Menu, PancackeMenu
from .waitress import Waitress


def run_pattern_example() -> None:
    """Run pattern example."""
    pancake_menu: Menu = PancackeMenu()
    diner_menu: Menu = DinerMenu()

    pancake_menu.add_item({"pancake": 1.99})
    pancake_menu.add_item({"waffle": 2.99})

    diner_menu.add_item(("spaghetti", 3.99))
    diner_menu.add_item(("meatballs", 4.99))

    waitress: Waitress = Waitress([pancake_menu, diner_menu])
    waitress.print_all_menus()


if __name__ == "__main__":
    run_pattern_example()
