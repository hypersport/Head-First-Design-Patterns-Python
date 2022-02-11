from command import Command


class MacroCommand(Command):
    def __init__(self, commands):
        self.commands = commands

    def excuse(self):
        for command in self.commands:
            command.excuse()

    def undo(self):
        for command in self.commands:
            command.undo()
