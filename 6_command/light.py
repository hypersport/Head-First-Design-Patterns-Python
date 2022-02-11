class Light:
    def __init__(self, location):
        self.location = location
        self.level = 0

    def on(self):
        self.level = 100
        print('Light is on')

    def off(self):
        self.level = 0
        print('Light is off')

    def dim(self, level):
        self.level = level
        if level == 0:
            self.off()
        else:
            print(f'Light is dimmed to {level}%')

    def get_level(self):
        return self.level
