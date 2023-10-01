from abc import ABC, abstractmethod


class Receiver(ABC):
    @abstractmethod
    def on(self) -> None:
        ...

    @abstractmethod
    def off(self) -> None:
        ...

    def __repr__(self) -> str:
        return self.__class__.__name__


class KitchenLight(Receiver):
    def on(self) -> None:
        print('Kitchen light is turned on.')

    def off(self) -> None:
        print('Kitchen light is turned off.')


class BedroomLight(Receiver):
    def on(self) -> None:
        print('Bedroom light is turned on.')

    def off(self) -> None:
        print('Bedroom light is turned off.')


class TV(Receiver):
    def on(self) -> None:
        print('TV is turned on.')

    def off(self) -> None:
        print('TV is turned off.')
