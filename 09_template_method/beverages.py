from abc import ABC, abstractmethod
from typing import final


class CaffeineBeverage(ABC):
    @final
    def prepare_recipe(self) -> None:
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @abstractmethod
    def brew(self) -> None:
        pass

    @abstractmethod
    def add_condiments(self) -> None:
        pass

    def boil_water(self) -> None:
        print("Boiling water")

    def pour_in_cup(self) -> None:
        print("Pouring into cup")


class Coffee(CaffeineBeverage):
    def brew(self) -> None:
        print("Dripping coffee through filter")

    def add_condiments(self) -> None:
        print("Adding sugar and milk")


class Tea(CaffeineBeverage):
    def brew(self) -> None:
        print("Steeping the tea")

    def add_condiments(self) -> None:
        print("Adding lemon")
