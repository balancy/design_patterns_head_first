"""Invoker class. It will handle commands queue and execute them one by one."""


from collections import deque

from .commands import Command


class Invoker:
    """Invoker class."""

    def __init__(self) -> None:
        """Initialize with empty commands queue."""
        self._commands: deque[Command] = deque()
        self._executed_commands: deque[Command] = deque()

    def set_commands(self, commands: deque[Command]) -> None:
        """Set commands queue."""
        self._commands = commands

    def set_command(self, command: Command) -> None:
        """Add a single command to the command queue."""
        self._commands.append(command)

    def execute_command(self) -> None:
        """Execute the first command in the command queue."""
        if self._commands:
            command = self._commands.popleft()
            print(f'"{command}" is executing')
            command.execute()
            self._executed_commands.append(command)

            print(f'"{command}" is executed')

    def undo_command(self) -> None:
        """Undo the last executed command."""
        if self._executed_commands:
            last_command = self._executed_commands.pop()
            print(f'"{last_command}" is undoing')
            last_command.undo()
            self._commands.appendleft(last_command)

            print(f'"{last_command}" is undone')

    @property
    def commands(self) -> deque[Command]:
        """Return commands queue."""
        return self._commands
