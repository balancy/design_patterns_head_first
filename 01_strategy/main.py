from .ducks import DecoyDuck, Duck, MaillardDuck, RubberDuck


def test_behaviour(duck: Duck) -> None:
    duck.display()
    duck.swim()
    duck.perform_fly()
    duck.perform_quack()
    print()


def run() -> None:
    duck_types = (MaillardDuck, RubberDuck, DecoyDuck)
    for duck in duck_types:
        test_behaviour(duck())


if __name__ == '__main__':
    run()
