class CdPlayer:
    def __init__(self, desc):
        self.description = desc
        self.current_track = 0
        self.title = ''

    def on(self):
        print(f'{self.description} on.')

    def off(self):
        print(f'{self.description} off.')

    def eject(self):
        self.title = ''
        print(f'{self.description} eject.')

    def play(self, param):
        if isinstance(param, str):
            self.title = param
            self.current_track = 0
            print(f'{self.description} playing "{self.title}".')
        elif isinstance(param, int):
            if not self.title:
                print(f'{self.description} cannot play track {param} no dvd inserted.')
            else:
                self.current_track = param
                print(f'{self.description} playing track {self.current_track} of "{self.title}".')

    def stop(self):
        self.current_track = 0
        print(f'{self.description} stopped "{self.title}".')

    def pause(self):
        print(f'{self.description} paused "{self.title}".')

    def __str__(self):
        return self.description
