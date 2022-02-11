class Hottub:
    def __init__(self):
        self.is_on = False
        self.temperature = 0

    def on(self):
        self.is_on = True

    def off(self):
        self.is_on = False

    def circulate(self):
        if self.is_on:
            print('Hottub is bubbling!')

    def jets_on(self):
        if self.is_on:
            print('Hottub jets are on')

    def jets_off(self):
        if self.is_on:
            print('Hottub jets are off')

    def set_temperature(self, temperature):
        if temperature > self.temperature:
            print(f'Hottub is heating to a steaming {temperature} degrees.')
        else:
            print(f'Hottub is cooling to {temperature} degrees.')
        self.temperature = temperature
