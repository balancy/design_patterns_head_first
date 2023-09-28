from .ducks import DecoyDuck, Duck, MaillardDuck, RubberDuck


def test_behaviour(duck: Duck) -> None:
    duck.display()
    duck.swim()
    duck.perform_fly()
    duck.perform_quack()
    print()


def run() -> None:
    ducks = (MaillardDuck, RubberDuck, DecoyDuck)
    for duck in ducks:
        test_behaviour(duck())


if __name__ == '__main__':
    run()
