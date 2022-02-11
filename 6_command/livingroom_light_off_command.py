from command import Command


class LivingroomLightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def excuse(self):
        self.light.off()

    def undo(self):
        self.light.on()
