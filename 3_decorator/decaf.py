from beverage import Beverage


class Decaf(Beverage):
    def __init__(self):
        self.description = 'Decaf Coffee'

    def cost(self):
        return 1.05
