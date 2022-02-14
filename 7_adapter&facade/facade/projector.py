class Projector:
    def __init__(self, desc):
        self.description = desc

    def on(self):
        print(f'{self.description} on.')

    def off(self):
        print(f'{self.description} off.')

    def wide_screen_mode(self):
        print(f'{self.description} in widescreen mode (16x9 aspect ratio).')

    def tv_mode(self):
        print(f'{self.description} in tv mode (4x3 aspect ratio).')

    def __str__(self):
        return self.description
