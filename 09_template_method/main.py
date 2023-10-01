from .beverages import CaffeineBeverage, Coffee, Tea


def run() -> None:
    tea: CaffeineBeverage = Tea()
    coffee: CaffeineBeverage = Coffee()

    print("Making tea...")
    tea.prepare_recipe()

    print("\nMaking coffee...")
    coffee.prepare_recipe()


if __name__ == "__main__":
    run()
