from beverage import Beverage


class HouseBlend(Beverage):
    def __init__(self):
        self.description = 'House Blend Coffee'

    def cost(self):
        return 0.89
