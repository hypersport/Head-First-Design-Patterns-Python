from command import Command


class TvOffCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def excuse(self):
        self.tv.off()

    def undo(self):
        self.tv.on()
