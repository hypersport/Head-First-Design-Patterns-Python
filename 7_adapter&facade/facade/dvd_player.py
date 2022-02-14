class DvdPlayer:
    def __init__(self, desc):
        self.description = desc
        self.current_track = 0
        self.movie = ''

    def on(self):
        print(f'{self.description} on.')

    def off(self):
        print(f'{self.description} off.')

    def eject(self):
        self.movie = ''
        print(f'{self.description} eject.')

    def play(self, param):
        if isinstance(param, str):
            self.movie = param
            self.current_track = 0
            print(f'{self.description} playing "{self.movie}".')
        elif isinstance(param, int):
            if not self.movie:
                print(f'{self.description} cannot play track {param} no dvd inserted.')
            else:
                self.current_track = param
                print(f'{self.description} playing track {self.current_track} of "{self.movie}".')

    def stop(self):
        self.current_track = 0
        print(f'{self.description} stopped "{self.movie}".')

    def pause(self):
        print(f'{self.description} paused "{self.movie}".')

    def set_two_channel_audio(self):
        print(f'{self.description} set two channel audio.')

    def set_surround_audio(self):
        print(f'{self.description} set surround audio.')

    def __str__(self):
        return self.description
