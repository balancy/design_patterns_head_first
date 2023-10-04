"""Custom iterator class."""

from __future__ import annotations


class Iterator:
    """Iterator class."""

    def __init__(self, collection: list[tuple[str, float]]) -> None:
        """Initialize iterator."""
        self._collection = collection
        self._index = 0

    def __iter__(self) -> Iterator:
        """Return iterator."""
        return self

    def __next__(self) -> tuple[str, float]:
        """Return next element."""
        if self._index >= len(self._collection):
            raise StopIteration
        current_element = self._collection[self._index]
        self._index += 1
        return current_element
