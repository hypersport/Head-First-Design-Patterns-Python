from command import Command


class HottubOnCommand(Command):
    def __init__(self, hottub):
        self.hottub = hottub

    def excuse(self):
        self.hottub.on()
        self.hottub.set_temperature(104)
        self.hottub.circulate()

    def undo(self):
        self.hottub.off()
