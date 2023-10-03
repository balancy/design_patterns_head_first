"""Main entrypoint for the Template method pattern example."""


from .beverages import CaffeineBeverage, Coffee, Tea


def run_pattern_example() -> None:
    """Test template method pattern example.

    Two implementation of caffeine beverages show using template of parent
    class.
    """
    tea: CaffeineBeverage = Tea()
    coffee: CaffeineBeverage = Coffee()

    print("Making tea...")
    tea.prepare_recipe()

    print("\nMaking coffee...")
    coffee.prepare_recipe()


if __name__ == "__main__":
    run_pattern_example()
