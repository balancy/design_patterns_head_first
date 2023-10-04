"""Abstract Menu class and 2 implementations."""

from abc import ABC, abstractmethod

from .iterators import MenuIterator


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
    def set_items(self, items) -> None:
        """Set all menu items (abstract method).

        All child classes must implement this method.
        """
        ...

    @abstractmethod
    def create_iterator(self) -> MenuIterator:
        """Create iterator for menu items (abstract method).

        All child classes must implement this method.
        """
        ...

    @property
    def description(self) -> str:
        """Return menu description."""
        return self._description

    @abstractmethod
    def __repr__(self) -> str:
        """Return menu representation.

        All child classes must implement this method.
        """
        ...


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

    def set_items(self, items: list[tuple[str, float]]) -> None:
        """Set all menu items."""
        self._menu_items = items

    def create_iterator(self) -> MenuIterator:
        """Create iterator for menu items."""
        return MenuIterator(self._menu_items)

    def __repr__(self) -> str:
        """Return menu representation."""
        return f'{self._description} with {len(self._menu_items)} items'


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

    def set_items(self, items: dict[str, float]) -> None:
        """Set all menu items."""
        self._menu_items = items

    def create_iterator(self) -> MenuIterator:
        """Create iterator for menu items."""
        return MenuIterator(list(self._menu_items.items()))

    def __repr__(self) -> str:
        """Return menu representation."""
        return f'{self._description} with {len(self._menu_items)} items'
