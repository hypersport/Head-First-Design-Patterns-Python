from command import Command


class StereoOnCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def excuse(self):
        self.stereo.on()

    def undo(self):
        self.stereo.off()
