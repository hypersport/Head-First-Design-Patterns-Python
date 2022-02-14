class Tuner:
    def __init__(self, desc):
        self.description = desc
        self.frequency = 0

    def on(self):
        print(f'{self.description} on.')

    def off(self):
        print(f'{self.description} off.')

    def set_frequency(self, frequency):
        print(f'{self.description} setting frequency to {frequency}.')
        self.frequency = frequency

    def set_am(self):
        print(f'{self.description} setting AM mode.')

    def set_fm(self):
        print(f'{self.description} setting FM mode.')

    def __str__(self):
        return self.description
