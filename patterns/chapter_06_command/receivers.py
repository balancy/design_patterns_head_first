"""Abstract receiver class and 3 its implementations."""

from abc import ABC, abstractmethod


class Receiver(ABC):
    """Abstract receiver class."""

    @abstractmethod
    def on(self) -> None:
        """Abstract method for turning the receiver on."""
        ...

    @abstractmethod
    def off(self) -> None:
        """Abstract method for turning the receiver off."""
        ...

    def __repr__(self) -> str:
        """Return the receiver representation."""
        return self.__class__.__name__


class KitchenLight(Receiver):
    """Kitchen light as receiver class implementation."""

    def on(self) -> None:
        """Turn the kitchen light on."""
        print('Kitchen light is turned on.')

    def off(self) -> None:
        """Turn the kitchen light off."""
        print('Kitchen light is turned off.')


class BedroomLight(Receiver):
    """Bedroom light as receiver class implementation."""

    def on(self) -> None:
        """Turn the bedroom light on."""
        print('Bedroom light is turned on.')

    def off(self) -> None:
        """Turn the bedroom light off."""
        print('Bedroom light is turned off.')


class TV(Receiver):
    """TV as receiver class implementation."""

    def on(self) -> None:
        """Turn the TV on."""
        print('TV is turned on.')

    def off(self) -> None:
        """Turn the TV off."""
        print('TV is turned off.')
