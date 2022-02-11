from command import Command


class StereoOnWithCDCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def excuse(self):
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)

    def undo(self):
        self.stereo.off()
