from no_command import NoCommand


class RemoteControl:
    def __init__(self):
        no_command = NoCommand()
        self.on_commands = [no_command] * 7
        self.off_commands = [no_command] * 7
        self.undo_command = no_command

    def set_command(self, slot, on_command, off_command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_pushed(self, slot):
        self.on_commands[slot].excuse()
        self.undo_command = self.on_commands[slot]

    def off_button_pushed(self, slot):
        self.off_commands[slot].excuse()
        self.undo_command = self.off_commands[slot]

    def undo_button_pushed(self):
        self.undo_command.undo()

    def __str__(self):
        result = ['\n------ Remote Control -------\n']
        for i, command in enumerate(self.on_commands):
            result.append(f'[slot {i}] {command.__class__.__name__}    '
                          f'{self.off_commands[i].__class__.__name__}\n')
        result.append(f'[undo] {self.undo_command.__class__.__name__}\n')
        return ' '.join(result)
