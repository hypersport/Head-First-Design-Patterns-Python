from command import Command


class LivingroomLightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def excuse(self):
        self.light.on()

    def undo(self):
        self.light.off()
