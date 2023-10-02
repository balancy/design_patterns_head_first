"""Main entrypoint module for strategy pattern example."""

from .ducks import DecoyDuck, Duck, MaillardDuck, RubberDuck


def print_duck_behaviour(duck: Duck) -> None:
    """Show duck behaviour, including swimming, flying and quacking."""
    duck.display()
    duck.swim()
    duck.perform_fly()
    duck.perform_quack()
    print()


def run_pattern_example() -> None:
    """Test strategy pattern.

    Different duck implementations demonstrate different behaviours.
    """
    for duck in (MaillardDuck(), RubberDuck(), DecoyDuck()):
        print_duck_behaviour(duck)


if __name__ == '__main__':
    run_pattern_example()
