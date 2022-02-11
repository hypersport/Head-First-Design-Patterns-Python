from command import Command


class TvOnCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def excuse(self):
        self.tv.on()
        self.tv.set_input_channel()

    def undo(self):
        self.tv.off()
