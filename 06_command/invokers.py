from collections import deque

from .commands import Command


class Invoker:
    def __init__(self) -> None:
        self._commands: deque[Command] = deque()
        self._executed_commands: deque[Command] = deque()

    def set_commands(self, commands: deque[Command]) -> None:
        self._commands = commands

    def set_command(self, command: Command) -> None:
        self._commands.append(command)

    def execute_command(self) -> None:
        if self._commands:
            command = self._commands.popleft()
            print(f'"{command}" is executing')
            command.execute()
            self._executed_commands.append(command)

            print(f'"{command}" is executed')

    def undo_command(self) -> None:
        if self._executed_commands:
            last_command = self._executed_commands.pop()
            print(f'"{last_command}" is undoing')
            last_command.undo()
            self._commands.appendleft(last_command)

            print(f'"{last_command}" is undone')

    @property
    def commands(self) -> deque[Command]:
        return self._commands
