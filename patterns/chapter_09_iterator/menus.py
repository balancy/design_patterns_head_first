"""Abstract Menu class and 2 implementations."""

from abc import ABC, abstractmethod

from .iterators import Iterator


class Menu(ABC):
    """Abstract Menu class."""

    _description: str

    @abstractmethod
    def add_item(self, item) -> None:
        """Add item to menu (abstract method).

        All child classes must implement this method.
        """
        ...

    @abstractmethod
    def create_iterator(self) -> Iterator:
        """Create iterator for menu items (abstract method).

        All child classes must implement this method.
        """
        ...

    @property
    def description(self) -> str:
        """Return menu description."""
        return self._description


class DinerMenu(Menu):
    """Diner menu class.

    Uses tuples to store menu items.
    """

    _description: str = 'Diner menu'

    def __init__(self) -> None:
        """Initialize menu."""
        self._menu_items: list[tuple[str, float]] = []

    def add_item(self, item: tuple[str, float]) -> None:
        """Add item to menu."""
        self._menu_items.append(item)

    def create_iterator(self) -> Iterator:
        """Create iterator for menu items."""
        return Iterator(self._menu_items)


class PancackeMenu(Menu):
    """Pancake menu class.

    Uses dict to store menu items.
    """

    _description = 'Pancake menu'

    def __init__(self) -> None:
        """Initialize menu."""
        self._menu_items: dict[str, float] = {}

    def add_item(self, item: dict[str, float]) -> None:
        """Add item to menu."""
        self._menu_items.update(item)

    def create_iterator(self) -> Iterator:
        """Create iterator for menu items."""
        return Iterator(list(self._menu_items.items()))
