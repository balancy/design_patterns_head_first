"""Iterator module."""

from __future__ import annotations

from .menus import DinerMenu, Menu, PancackeMenu
from .waitress import Waitress


def run_pattern_example() -> None:
    """Run pattern example."""
    pancake_menu: Menu = PancackeMenu()
    pancake_menu.set_items({"pancake": 1.99, "waffle": 2.99})

    diner_menu: Menu = DinerMenu()
    diner_menu.set_items([("spaghetti", 3.99), ("meatballs", 4.99)])

    waitress: Waitress = Waitress([pancake_menu, diner_menu])
    waitress.print_all_menus()


if __name__ == "__main__":
    run_pattern_example()
