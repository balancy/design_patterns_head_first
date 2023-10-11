"""Module for testing pattern "Composite"."""


import pytest

from patterns.chapter_09_composite.humains import AbstractHumain, Child, Humain


@pytest.mark.parametrize(
    ('parent', 'children', 'expected_names_in_family_tree'),
    [
        (
            Humain('father'),
            [Child('son'), Child('daughter')],
            ['father', 'son', 'daughter'],
        ),
    ],
)
def test_all_members_in_family_tree(
    capsys,
    parent: AbstractHumain,
    children: list[AbstractHumain],
    expected_names_in_family_tree: list[str],
) -> None:
    """Test if all family mambers are in family tree."""
    for child in children:
        parent.add_child(child)

    print(parent.family_tree)
    captured = capsys.readouterr()

    for expected_name in expected_names_in_family_tree:
        assert expected_name in captured.out
