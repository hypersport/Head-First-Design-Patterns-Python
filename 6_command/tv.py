class Tv:
    def __init__(self, location):
        self.location = location
        self.channel = ''

    def on(self):
        print(f'{self.location} TV is on.')

    def off(self):
        print(f'{self.location} TV is off.')

    def set_input_channel(self):
        self.channel = 3
        print(f'{self.location} TV channel is set for DVD')
