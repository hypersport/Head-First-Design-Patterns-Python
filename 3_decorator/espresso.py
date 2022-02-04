from beverage import Beverage


class Espresso(Beverage):
    def __init__(self):
        self.description = 'Espresso'

    def cost(self):
        return 1.99
