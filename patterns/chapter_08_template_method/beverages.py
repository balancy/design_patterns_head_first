"""Abstract caffeine beverage class two its implementations."""

from abc import ABC, abstractmethod
from typing import final


class CaffeineBeverage(ABC):
    """Abstract class for caffeine beverages."""

    @final
    def prepare_recipe(self) -> None:
        """Prepare recipe.

        It includes all steps of making caffeine beverage and it could not be
        overriden in child classes.
        """
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @abstractmethod
    def brew(self) -> None:
        """Brew beverage.

        Abstract method. Should be implemented in child classes.
        """
        pass

    @abstractmethod
    def add_condiments(self) -> None:
        """Add condiments.

        Abstract method. Should be implemented in child classes.
        """
        pass

    def boil_water(self) -> None:
        """Boil water."""
        print("Boiling water")

    def pour_in_cup(self) -> None:
        """Pour beverage into cup."""
        print("Pouring into cup")


class Coffee(CaffeineBeverage):
    """Coffee beverage."""

    def brew(self) -> None:
        """Brew coffee."""
        print("Dripping coffee through filter")

    def add_condiments(self) -> None:
        """Add condiments to coffee."""
        print("Adding sugar and milk")


class Tea(CaffeineBeverage):
    """Tea beverage."""

    def brew(self) -> None:
        """Brew tea."""
        print("Steeping the tea")

    def add_condiments(self) -> None:
        """Add condiments to tea."""
        print("Adding lemon")
