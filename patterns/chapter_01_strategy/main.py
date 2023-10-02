"""Main entrypoint module for strategy pattern."""

from .ducks import DecoyDuck, Duck, MaillardDuck, RubberDuck


def print_duck_behaviour(duck: Duck) -> None:
    """Show duck behaviour, including swimming, flying and quacking."""
    duck.display()
    duck.swim()
    duck.perform_fly()
    duck.perform_quack()
    print()


def test_drive() -> None:
    """Run every concrete duck implementation behaviour test."""
    for duck in (MaillardDuck(), RubberDuck(), DecoyDuck()):
        print_duck_behaviour(duck)


if __name__ == '__main__':
    test_drive()
