from command import Command


class StereoOffCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def excuse(self):
        self.stereo.off()

    def undo(self):
        self.stereo.on()
