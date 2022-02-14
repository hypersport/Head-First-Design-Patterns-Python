class TheaterLights:
    def __init__(self, desc):
        self.description = desc

    def on(self):
        print(f'{self.description} on.')

    def off(self):
        print(f'{self.description} off.')

    def dim(self, level):
        print(f'{self.description} dimming to {level}%.')

    def __str__(self):
        return self.description
