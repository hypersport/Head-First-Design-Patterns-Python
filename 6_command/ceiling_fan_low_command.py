from command import Command
from ceiling_fan import CeilingFanSpeed


class CeilingFanLowCommand(Command):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed = CeilingFanSpeed.OFF

    def excuse(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.low()

    def undo(self):
        if self.prev_speed == CeilingFanSpeed.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == CeilingFanSpeed.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == CeilingFanSpeed.LOW:
            self.ceiling_fan.low()
        else:
            self.ceiling_fan.off()
