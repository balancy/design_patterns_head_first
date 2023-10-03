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


class Device(Receiver):
    """Device as Receiver class implementation."""

    def __init__(self) -> None:
        """Initialize with the default status."""
        self._is_on: bool = False

    @property
    def is_on(self) -> bool:
        """Return the status of the device."""
        return self._is_on


class KitchenLight(Device):
    """Kitchen light as receiver class implementation."""

    def on(self) -> None:
        """Turn the kitchen light on."""
        self._is_on = True
        print('Kitchen light is turned on.')

    def off(self) -> None:
        """Turn the kitchen light off."""
        self._is_on = False
        print('Kitchen light is turned off.')


class BedroomLight(Device):
    """Bedroom light as receiver class implementation."""

    def on(self) -> None:
        """Turn the bedroom light on."""
        self._is_on = True
        print('Bedroom light is turned on.')

    def off(self) -> None:
        """Turn the bedroom light off."""
        self._is_on = False
        print('Bedroom light is turned off.')


class TV(Device):
    """TV as receiver class implementation."""

    def on(self) -> None:
        """Turn the TV on."""
        self._is_on = True
        print('TV is turned on.')

    def off(self) -> None:
        """Turn the TV off."""
        self._is_on = False
        print('TV is turned off.')
