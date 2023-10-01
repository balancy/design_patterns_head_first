from .ducks import Duck
from .turkeys import Turkey


class TurkeyObjectAdapter(Duck):
    def __init__(self, turkey: Turkey) -> None:
        self.turkey = turkey

    def quack(self) -> None:
        self.turkey.gobble()

    def fly(self) -> None:
        for _ in range(5):
            self.turkey.short_fly()


class TurkeyClassAdapter(Turkey, Duck):
    def quack(self) -> None:
        self.gobble()

    def fly(self) -> None:
        for _ in range(5):
            self.short_fly()

    def gobble(self) -> None:
        print('Gobble gobble')

    def short_fly(self) -> None:
        print('I\'m flying a short distance')
