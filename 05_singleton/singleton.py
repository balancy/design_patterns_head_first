from typing import Self


class Singleton(object):
    def __new__(cls) -> Self:
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} #{id(self)}>'
