"""Module for testing pattern "Singleton"."""


from patterns.chapter_05_singleton.singleton import Singleton


def test_singleton() -> None:
    """Test signleton pattern.

    Two created instances should be the same object.
    """
    s1 = Singleton()
    s2 = Singleton()

    assert str(s1) == str(s2)
