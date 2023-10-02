"""Module for testing pattern "Strategy"."""

import pytest

from patterns.chapter_01_strategy.ducks import (
    DecoyDuck,
    Duck,
    MaillardDuck,
    RubberDuck,
)
from patterns.chapter_01_strategy.main import print_duck_behaviour


@pytest.mark.parametrize(
    ('duck', 'produced_sound'),
    [
        (DecoyDuck(), '<< Silence >>'),
        (MaillardDuck(), 'Quack'),
        (RubberDuck(), 'Squeak'),
    ],
)
def test_pattern_as_black_box(capsys, duck: Duck, produced_sound: str) -> None:
    """Test pattern as black box."""
    print_duck_behaviour(duck)
    captured = capsys.readouterr()

    assert produced_sound in captured.out
