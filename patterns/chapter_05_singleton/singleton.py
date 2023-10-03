"""Implementation of SIngleton class."""


from __future__ import annotations


class Singleton(object):
    """Singleton class implementation."""

    def __new__(cls) -> Singleton:
        """Return singleton instance.

        If instance is not created, create it and return it.
        If instance is already created, return it.
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __repr__(self) -> str:
        """Return object representation."""
        return f'<{self.__class__.__name__} #{id(self)}>'
