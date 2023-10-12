"""Main entrypoint for the Composite pattern example."""

from .humans import Child, Human


def test_pattern_example() -> None:
    """Test composite pattern example.

    Family tree is displayed correctly with Humain as composite and Child as
    leaf.
    """
    grandfather = Human('Grandfather')

    mother = Human('Mother')
    taunt = Child('Taunt')
    uncle = Child('Uncle')
    grandfather.add_child(mother)
    grandfather.add_child(taunt)
    grandfather.add_child(uncle)

    me = Child('Me')
    brother = Human('Brother')
    sister = Human('Sister')
    mother.add_child(me)
    mother.add_child(brother)
    mother.add_child(sister)

    son_of_brother = Child('Son of brother')
    brother.add_child(son_of_brother)

    daughter_of_sister = Child('Daughter of sister')
    sister.add_child(daughter_of_sister)

    print('Family tree of grandfather:')
    print(grandfather.family_tree)


if __name__ == "__main__":
    test_pattern_example()
