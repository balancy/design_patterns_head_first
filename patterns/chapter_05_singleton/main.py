"""Main entrypoint for the Singleton pattern example."""


from .singleton import Singleton


def run_pattern_example() -> None:
    """Test singleton example.

    Two created class instances should be the same object.
    """
    s1 = Singleton()
    s2 = Singleton()
    print(f'Are {s1} and {s2} the same instances? {s1 is s2}')


if __name__ == '__main__':
    run_pattern_example()
