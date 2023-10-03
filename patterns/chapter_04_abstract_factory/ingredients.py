"""Ingredients for pizza."""

from abc import ABC, abstractmethod


class Dough(ABC):
    """Abstract dough class."""

    @abstractmethod
    def __repr__(self) -> str:
        """Abstract method for dough representation.

        All child classes must implement this method.
        """
        ...


class ThinCrustDough(Dough):
    """Thin crust dough class."""

    def __repr__(self) -> str:
        """Return dough representation."""
        return 'Thin Crust Dough'


class ThickCrustDough(Dough):
    """Thick crust dough class."""

    def __repr__(self) -> str:
        """Return dough representation."""
        return 'Thick Crust Dough'


class Sauce(ABC):
    """Abstract sauce class."""

    @abstractmethod
    def __repr__(self) -> str:
        """Abstract method for sauce representation.

        All child classes must implement this method.
        """
        ...


class MarinaraSauce(Sauce):
    """Marinara sauce class."""

    def __repr__(self) -> str:
        """Return sauce representation."""
        return 'Marinara Sauce'


class PlumTomatoSauce(Sauce):
    """Plum tomato sauce class."""

    def __repr__(self) -> str:
        """Return sauce representation."""
        return 'Plum Tomato Sauce'


class Cheese(ABC):
    """Abstract cheese class."""

    @abstractmethod
    def __repr__(self) -> str:
        """Abstract method for cheese representation.

        All child classes must implement this method.
        """
        ...


class MozarellaCheese(Cheese):
    """Mozarella cheese class."""

    def __repr__(self) -> str:
        """Return cheese representation."""
        return 'Mozarella Cheese'


class ReggianoCheese(Cheese):
    """Reggiano cheese class."""

    def __repr__(self) -> str:
        """Return cheese representation."""
        return 'Reggiano Cheese'


class Pepperoni(ABC):
    """Abstract pepperoni class."""

    @abstractmethod
    def __repr__(self) -> str:
        """Abstract method for pepperoni representation.

        All child classes must implement this method.
        """
        ...


class SlicedPepperoni(Pepperoni):
    """Sliced pepperoni class."""

    def __repr__(self) -> str:
        """Return pepperoni representation."""
        return 'Sliced Pepperoni'


class Clams(ABC):
    """Abstract clams class."""

    @abstractmethod
    def __repr__(self) -> str:
        """Abstract method for clams representation.

        All child classes must implement this method.
        """
        ...


class FrozenClams(Clams):
    """Frozen clams class."""

    def __repr__(self) -> str:
        """Return clams representation."""
        return 'Frozen Clams'


class FreshClams(Clams):
    """Fresh clams class."""

    def __repr__(self) -> str:
        """Return clams representation."""
        return 'Fresh Clams'


class Veggie(ABC):
    """Abstract veggie class."""

    @abstractmethod
    def __repr__(self) -> str:
        """Abstract method for veggie representation.

        All child classes must implement this method.
        """
        ...


class Veggies:
    """Veggies class."""

    def __init__(self, ingredients) -> None:
        """Initialize ingredients."""
        self._ingredients = ingredients

    def __repr__(self) -> str:
        """Return veggies representation."""
        return ', '.join(self._ingredients)


class Garlic(Veggie):
    """Garlic class."""

    def __repr__(self) -> str:
        """Return garlic representation."""
        return 'Garlic'


class Onion(Veggie):
    """Onion class."""

    def __repr__(self) -> str:
        """Return onion representation."""
        return 'Onion'


class Mushroom(Veggie):
    """Mushroom class."""

    def __repr__(self) -> str:
        """Return mushroom representation."""
        return 'Mushroom'


class RedPepper(Veggie):
    """Red pepper class."""

    def __repr__(self) -> str:
        """Return red pepper representation."""
        return 'Red Pepper'
