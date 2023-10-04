"""Custom iterator class."""

from __future__ import annotations

from abc import ABC
from typing import Any


class Iterator(ABC):
    """Abstract iterator class."""

    def __iter__(self) -> Iterator:
        """Return iterator."""
        return self

    def __next__(self) -> Any:
        """Return next element (Abstract class).

        All child classes must implement this method.
        """
        ...


class MenuIterator:
    """Menu iterator class."""

    def __init__(self, collection: list[tuple[str, float]]) -> None:
        """Initialize iterator."""
        self._collection = collection
        self._index = 0

    def __iter__(self) -> MenuIterator:
        """Return iterator."""
        return self

    def __next__(self) -> tuple[str, float]:
        """Return next element."""
        if self._index >= len(self._collection):
            raise StopIteration
        current_element = self._collection[self._index]
        self._index += 1
        return current_element
