from command import Command


class HottubOffCommand(Command):
    def __init__(self, hottub):
        self.hottub = hottub

    def excuse(self):
        self.hottub.set_temperature(98)
        self.hottub.off()

    def undo(self):
        self.hottub.on()
