class PopcornPopper:
    def __init__(self, desc):
        self.description = desc

    def on(self):
        print(f'{self.description} on.')

    def off(self):
        print(f'{self.description} off.')

    def pop(self):
        print(f'{self.description} popping popcorn!')

    def __str__(self):
        return self.description
