class Amplifier:
    def __init__(self, desc):
        self.description = desc
        self.cd_player = None
        self.dvd_player = None
        self.tuner = None

    def on(self):
        print(f'{self.description} on.')

    def off(self):
        print(f'{self.description} off.')

    def set_stereo_sound(self):
        print(f'{self.description} stereo mode on.')

    def set_surround_sound(self):
        print(f'{self.description} surround sound on (5 speakers, 1 subwoofer).')

    def set_volume(self, level):
        print(f'{self.description} setting tuner to {level}.')

    def set_cd(self, cd):
        print(f'{self.description} setting CD player to {cd}.')
        self.cd_player = cd

    def set_dvd(self, dvd):
        print(f'{self.description} setting DVD player to {dvd}.')
        self.dvd_player = dvd

    def set_tuner(self, tuner):
        print(f'{self.description} setting tuner player to {tuner}.')
        self.tuner = tuner

    def __str__(self):
        return self.description
