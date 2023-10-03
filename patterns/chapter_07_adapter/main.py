"""Main entrypoint for the Adapter pattern example."""

from .adapters import TurkeyClassAdapter, TurkeyObjectAdapter
from .ducks import Duck, MallardDuck
from .turkeys import Turkey, WildTurkey


def run_pattern_example() -> None:
    """Test adapter pattern example.

    Methods of one object sould be translated to methods of another object via
    adapter.
    """
    mallard_duck: Duck = MallardDuck()
    wild_turkey: Turkey = WildTurkey()

    turkey_object_adapter: Duck = TurkeyObjectAdapter(wild_turkey)
    turkey_class_adapter: TurkeyClassAdapter = TurkeyClassAdapter()

    print('The Turkey says...')
    wild_turkey.gobble()
    wild_turkey.short_fly()

    print()
    print('The Duck says...')
    mallard_duck.quack()
    mallard_duck.fly()

    print()
    print('The Turkey object adapter says...')
    turkey_object_adapter.quack()
    turkey_object_adapter.fly()

    print()
    print('The Turkey class adapter says...')
    turkey_class_adapter.quack()
    turkey_class_adapter.fly()


if __name__ == '__main__':
    run_pattern_example()
