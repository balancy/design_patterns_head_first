"""Abstract human class and 2 implementations.

Humain could have children, Child could not.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractHuman(ABC):
    """Abstract human class."""

    def __init__(self, name: str) -> None:
        """Initialize human."""
        self._name = name

    @property
    def parent(self) -> AbstractHuman | None:
        """Return parent of human."""
        return self._parent

    @parent.setter
    def parent(self, parent: AbstractHuman | None) -> None:
        """Set parent of human."""
        self._parent = parent

    def add_child(self, human: AbstractHuman) -> None:
        """Add child to human."""
        pass

    def remove_child(self, human: AbstractHuman) -> None:
        """Remove child from human."""
        pass

    def is_composite(self) -> bool:
        """Return True if human is composite."""
        return False

    @property
    @abstractmethod
    def family_tree(self) -> str:
        """Return family tree of human for print."""
        pass


class Child(AbstractHuman):
    """Child human class.

    Implementation of abstract human class.
    """

    def __init__(self, name: str) -> None:
        """Initialize child."""
        self._name = name

    @property
    def family_tree(self) -> str:
        """Return child's name."""
        return self._name


class Human(AbstractHuman):
    """Humain class.

    Implementation of abstract human class.
    """

    def __init__(self, name: str) -> None:
        """Initialize human."""
        self._children: list[AbstractHuman] = []
        self._name = name

    def add_child(self, human: AbstractHuman) -> None:
        """Add child to human."""
        self._children.append(human)
        human.parent = self

    def remove_child(self, human: AbstractHuman) -> None:
        """Remove child from human."""
        self._children.remove(human)
        human.parent = None

    def is_composite(self) -> bool:
        """Humain instance is composite."""
        return True

    @property
    def family_tree(self) -> str:
        """Return family tree of human."""
        return (
            f'{self._name} '
            f'({", ".join(child.family_tree for child in self._children)})'
        )
