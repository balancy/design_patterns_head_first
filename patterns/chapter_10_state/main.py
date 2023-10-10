"""State module."""

from .gumball_machine import GumballMachine


def run_pattern_example() -> None:
    """Run pattern example."""
    machine = GumballMachine(3)

    print()
    print('Trying to manipulate the machine without coins')
    machine.turn_crunk()
    machine.dispense()
    machine.eject_quarter()

    print()
    print('Trying to insert two coins')
    machine.insert_quarter()
    machine.insert_quarter()

    print()
    print('Trying to eject coin two times')
    machine.eject_quarter()
    machine.eject_quarter()

    print()
    print('Trying to turn crank two times')
    machine.insert_quarter()
    machine.turn_crunk()
    machine.turn_crunk()

    print()
    print('Trying to dispense gumball two times')
    machine.dispense()
    machine.dispense()

    print()
    print('Use machine the normal way')
    machine.insert_quarter()
    machine.turn_crunk()
    machine.dispense()
    machine.insert_quarter()
    machine.turn_crunk()
    machine.dispense()

    print()
    print('Trying to manipulate the sold out machine')
    machine.insert_quarter()
    machine.turn_crunk()
    machine.dispense()


if __name__ == "__main__":
    run_pattern_example()
