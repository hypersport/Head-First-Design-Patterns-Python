class Stereo:
    def __init__(self, location):
        self.location = location

    def on(self):
        print(f'{self.location} stereo is on.')

    def off(self):
        print(f'{self.location} stereo is off.')

    def set_cd(self):
        print(f'{self.location} stereo is set for CD input.')

    def set_dvd(self):
        print(f'{self.location} stereo is set for DVD input.')

    def set_radio(self):
        print(f'{self.location} stereo is set for Radio.')

    def set_volume(self, volume):
        print(f'{self.location} stereo is set for DVD input {volume}.')
