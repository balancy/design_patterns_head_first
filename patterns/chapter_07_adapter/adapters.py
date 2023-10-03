"""Two implementations of adapter pattern.

One uses composition, the other uses multiple inheritance.
"""

from .ducks import Duck
from .turkeys import Turkey


class TurkeyObjectAdapter(Duck):
    """Adapter class that uses composition."""

    def __init__(self, turkey: Turkey) -> None:
        """Initialize with a turkey instance."""
        self.turkey = turkey

    def quack(self) -> None:
        """Quack method implementation."""
        self.turkey.gobble()

    def fly(self) -> None:
        """Fly method implementation."""
        for _ in range(5):
            self.turkey.short_fly()


class TurkeyClassAdapter(Turkey, Duck):
    """Adapter class that uses multiple inheritance."""

    def quack(self) -> None:
        """Quack method implementation."""
        self.gobble()

    def fly(self) -> None:
        """Fly method implementation."""
        for _ in range(5):
            self.short_fly()

    def gobble(self) -> None:
        """Gobble method implementation."""
        print('Gobble gobble')

    def short_fly(self) -> None:
        """Short fly method implementation."""
        print('I\'m flying a short distance')
