"""Abstract humain class and 2 implementations.

Humain could have children, Child could not.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractHumain(ABC):
    """Abstract humain class."""

    def __init__(self, name: str) -> None:
        """Initialize humain."""
        self._name = name

    @property
    def parent(self) -> AbstractHumain | None:
        """Return parent of humain."""
        return self._parent

    @parent.setter
    def parent(self, parent: AbstractHumain | None) -> None:
        """Set parent of humain."""
        self._parent = parent

    def add_child(self, humain: AbstractHumain) -> None:
        """Add child to humain."""
        pass

    def remove_child(self, humain: AbstractHumain) -> None:
        """Remove child from humain."""
        pass

    def is_composite(self) -> bool:
        """Return True if humain is composite."""
        return False

    @property
    @abstractmethod
    def family_tree(self) -> str:
        """Return family tree of humain for print."""
        pass


class Child(AbstractHumain):
    """Child humain class.

    Implementation of abstract humain class.
    """

    def __init__(self, name: str) -> None:
        """Initialize child."""
        self._name = name

    @property
    def family_tree(self) -> str:
        """Return child's name."""
        return self._name


class Humain(AbstractHumain):
    """Humain class.

    Implementation of abstract humain class.
    """

    def __init__(self, name: str) -> None:
        """Initialize humain."""
        self._children: list[AbstractHumain] = []
        self._name = name

    def add_child(self, humain: AbstractHumain) -> None:
        """Add child to humain."""
        self._children.append(humain)
        humain.parent = self

    def remove_child(self, humain: AbstractHumain) -> None:
        """Remove child from humain."""
        self._children.remove(humain)
        humain.parent = None

    def is_composite(self) -> bool:
        """Humain instance is composite."""
        return True

    @property
    def family_tree(self) -> str:
        """Return family tree of humain."""
        return (
            f'{self._name} '
            f'({", ".join(child.family_tree for child in self._children)})'
        )
