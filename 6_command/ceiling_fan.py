import enum


class CeilingFanSpeed(enum.Enum):
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0


class CeilingFan:
    def __init__(self, location):
        self.location = location
        self.speed = CeilingFanSpeed.OFF

    def high(self):
        self.speed = CeilingFanSpeed.HIGH
        print(f'{self.location} ceiling fan is on high.')

    def medium(self):
        self.speed = CeilingFanSpeed.MEDIUM
        print(f'{self.location} ceiling fan is on medium.')

    def low(self):
        self.speed = CeilingFanSpeed.LOW
        print(f'{self.location} ceiling fan is on low.')

    def off(self):
        self.speed = CeilingFanSpeed.OFF
        print(f'{self.location} ceiling fan is off')

    def get_speed(self):
        return self.speed
