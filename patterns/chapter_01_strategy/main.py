from .ducks import DecoyDuck, Duck, MaillardDuck, RubberDuck


def show_duck_behaviour(duck: Duck) -> None:
    duck.display()
    duck.swim()
    duck.perform_fly()
    duck.perform_quack()
    print()


def test_drive() -> None:
    for duck in (MaillardDuck(), RubberDuck(), DecoyDuck()):
        show_duck_behaviour(duck)


if __name__ == '__main__':
    test_drive()
