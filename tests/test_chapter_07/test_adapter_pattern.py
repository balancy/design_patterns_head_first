"""Module for testing pattern "Pattern"."""


from patterns.chapter_07_adapter.adapters import TurkeyObjectAdapter
from patterns.chapter_07_adapter.ducks import Duck
from patterns.chapter_07_adapter.turkeys import WildTurkey


def test_object_adapter_pattern(capsys) -> None:
    """Test object adapter pattern."""
    wild_turkey = WildTurkey()
    turkey_to_duck: Duck = TurkeyObjectAdapter(wild_turkey)

    turkey_to_duck.quack()
    turkey_to_duck.fly()

    captured = capsys.readouterr()

    assert wild_turkey.sound_produced in captured.out
    assert wild_turkey.flying_behaviour in captured.out
